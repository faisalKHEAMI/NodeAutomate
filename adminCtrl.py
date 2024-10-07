import paramiko
import PySimpleGUI as des

# Path to your SSH private key
key_path = '/Users/faisal/Downloads/website.pem'

# Create a Paramiko SSH client
ssh = paramiko.SSHClient()

# Load SSH host keys
ssh.load_system_host_keys()

# Set policy to automatically add the server's host key (for first-time connection)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def check_pid(window):
    message = ""  
    try:
        # Execute a command to check if 'node' is running
        stdin, stdout, stderr = ssh.exec_command('pgrep node')
        
        # Read and decode the output, split into list of PIDs
        pids_list = stdout.read().decode().strip().split()

        # Check if there are any Node.js processes running
        if pids_list:
            message = "Node.js is running with PIDs: {}".format(", ".join(pids_list))
            window['-Nodepids-'].update(message)
            print(message)
            kill_second_pid(pids_list, window)
        else: 
            message = "No Node.js processes are running."
            window['-Nodepids-'].update(message)

    except Exception as e:
        message = f"Error: {e}"
        window['-Nodepids-'].update(message, text_color='red')

def kill_second_pid(pids_list, window):
    message = ""  
    try:
        if pids_list:
            if len(pids_list) > 1:
                second_pid = pids_list[1]  # Get the second PID
                ssh.exec_command(f'sudo kill -9 {second_pid}')
                message = f"Killed Node.js process with PID: {second_pid}"
            else:
                message = "No second PID to kill."
        else:
            message = "No Node.js processes are running."

        # Update the window with process status
        window['-Nodekilled-'].update(message)
    except Exception as e:
        message = f"Error: {e}"
        window['-Nodekilled-'].update(message, text_color='red')

def start_node(window):
    message = ""  
    try:
        # Start the Node.js application
        ssh.exec_command(f'sudo node twilio-app/sendMessage.js')
        message = "Server Running"
        window['-ServerStatus-'].update(message)
    except Exception as e:
        message = f"Error: {e}"
        window['-ServerStatus-'].update(message, text_color='red')

def connectToServer(hostname, window):
    message = ""  
    try:
        # Connect to the EC2 instance
        ssh.connect(
            hostname='ec2-3-19-27-169.us-east-2.compute.amazonaws.com',
            username='ec2-user',
            key_filename=key_path
        )
        print("Connected to the server.")
        # Update the window with connection status
        message = "SSH connection successful."
        window['-SSHSTATUS-'].update(message, background_color='white', text_color='green')

        check_pid(window)
        start_node(window)

    except Exception as e:
        # Update the window with error message
        message = f"Error: {e}"
        window['-SSHSTATUS-'].update(message, text_color='red')

def close_connection(window):
    try:
        # Close the SSH connection
        check_pid(window)
        ssh.close()
        window['-SSHSTATUS-'].update("SSH connection closed.")
    except Exception as e:
        window['-SSHSTATUS-'].update(f"Error closing connection: {e}", text_color='red')


# Layout for the GUI
layout = [
    [des.Text('Enter EC2 US East server IP address')],
    [des.Input(default_text='3-19-27-169', key='-IPINPUT-')],
    [des.Text('Pem file path')],
    [des.Input(default_text=key_path, key='-FINPUT-')],
    [des.Button('Connect', key='-CONNECT-')],
    [des.Button('Disconnect', key='-DISCONNECT-')],
    [des.Text('', key='-SSHSTATUS-')],  # Status text
    [des.Text('', key='-Nodepids-')],
    [des.Text('', key='-Nodekilled-')],
    [des.Text('', key='-ServerStatus-')]
]

window = des.Window('Server Node Kill', layout)

# Event loop to capture input and connect
while True:
    event, values = window.read()

    if event == des.WIN_CLOSED:  # Close window event
        break
    if event == '-CONNECT-':  # Connect button pressed
        # Get the user input for the IP address
        ip_address = values['-IPINPUT-']
        key_path = values['-FINPUT-']
        # Call the connect function and pass the window to update the status
        connectToServer(ip_address, window)
    if event == '-DISCONNECT-':  # Kill ssh
        close_connection(window)

window.close()
