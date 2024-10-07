# NodeAutomate
Made this app because to automate the start/kill of my node on my remote server 
# Server Node Kill - SSH Manager

This Python application uses `Paramiko` to manage SSH connections to an EC2 instance and `PySimpleGUI` to create a simple 
GUI for monitoring and managing Node.js processes. The app can connect to a remote EC2 server, check if any Node.js 
processes are running, kill the second process if found, and start a Node.js application.

## Features
- **SSH Connection**: Establishes an SSH connection to a specified EC2 instance using a `.pem` private key.
- **Node.js Process Monitoring**: Checks if Node.js processes are running on the server.
- **Process Management**: Kills the second Node.js process if multiple instances are found.(First node is the server's node)
- **Node.js Application Startup**: Starts a Node.js application on the remote server.
- **Simple GUI**: Provides an easy-to-use interface for users to connect, monitor, and manage processes.

## Requirements

- Python 3.6+
- `paramiko` library for SSH connections
- `PySimpleGUI` library for the GUI interface

## Installation

1. Clone the repository:
    git clone https://github.com/faisalkheami/nodeAutomate

2. Install dependencies:
    pip install paramiko pysimplegui


3. Ensure that your SSH private key (e.g., `.pem` file) is stored on your machine. Update the `key_path` in the script to point to this key.

## Usage

1. Run the Python script:
    python server_node_kill.py
or try
    python3
   
3. A GUI will appear prompting you to enter the EC2 server's IP address. The default is set to `3-19-27-169`.

4. Click **Connect** to establish the SSH connection.

5. The app will check for any running Node.js processes:
   - If found, it will display the PIDs of the running processes and kill the second one (if applicable).
   - If not found, it will display a message indicating that no processes are running.

6. Click **Disconnect** to close the SSH connection.

## Running on Windows

### Ensure the following steps are completed:

- Update the `key_path` to the correct path for your SSH key. Use raw string notation for Windows file paths, e.g.:

    key_path = r'C:\path\to\your\website.pem'


- Ensure that **OpenSSH Client** is installed on your Windows machine. You can install it via **Settings > Apps > Optional Features**.

- To run the script:

    python server_node_kill.py
or try
    python3

### Optional: Create an Executable

If you'd like to create a standalone executable for easier distribution on Windows:

pip install pyinstaller
pyinstaller --onefile server_node_kill.py
This will generate an .exe file that you can run without needing Python installed.

Troubleshooting
SSH Connection Issues: Ensure your EC2 instance is reachable and that your .pem key file has the correct permissions.
Node.js Not Found: Ensure Node.js is installed and running on your EC2 instance.
Firewalls: Ensure Windows firewall or network settings don’t block outbound SSH connections.
Contributing
Feel free to fork this repository, open issues, or make pull requests if you'd like to contribute.

License
This project is licensed under the MIT License - see the LICENSE file for details.



### Key Sections:
- **Project Overview**: A brief introduction to the functionality.
- **Requirements**: The libraries and environment needed.
- **Installation**: Instructions on cloning the repo and setting up dependencies.
- **Usage**: Steps to run the app, along with notes on using the GUI.
- **Running on Windows**: Special instructions for Windows users, including making the app executable.
- **Troubleshooting**: Basic guidelines to resolve common issues.
- **Contributing & License**: Information on contributions and the license.

Make sure to replace placeholders like the repository URL and username if you're publishin
