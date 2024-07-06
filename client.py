import socket

# Define the server's host and port to connect to
HOST = '127.0.0.1'
PORT = 65432

# Create a socket object with IPv4 and TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f'Connected to server at {HOST}:{PORT}')

    while True:
        # Get user input to send to the server
        message = input('Enter message to send (or type "exit" to close): ')
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())
        # Receive the response from the server
        data = client_socket.recv(1024)
        print(f'Received from server: {data.decode()}')

print('Disconnected from server')
