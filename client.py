import socket

# CONSTANTS
# Define the server's host and port to connect to.
# In this example, we're connecting to a server running on the same machine (localhost),
# hence the IP address is 127.0.0.1
HOST = '127.0.0.1'
# The port number can range from 1 to 65535, in this case, we're using 65432.
PORT = 65432

# Create a socket object with IPv4 and TCP
# AF_INET corresponds to IPv4 and SOCK_STREAM corresponds to TCP.
# 'with' keyword ensures that the socket is properly closed when done, even in case of an error.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Establishes a TCP connection to the server
    client_socket.connect((HOST, PORT))
    print(f'Connected to server at {HOST}:{PORT}')

    # Main loop to send/receive messages
    while True:
        # Get user input to send to the server
        # 'input' function is used for interactive user input from the console.
        message = input('Enter message to send (or type "exit" to close): ')
        # If user types 'exit', the client will stop
        if message.lower() == 'exit':
            break

        # We use the 'sendall' method to ensure that all the data gets sent in TCP
        # The message is encoded to bytes for transmission using TCP/IP.
        client_socket.sendall(message.encode())

        # Receive the response from the server
        # The 'recv' function reads at most 1024 bytes from the received data.
        data = client_socket.recv(1024)
        # The data received from the server is decoded back into string format for readability.
        print(f'Received from server: {data.decode()}')

# Connection is closed upon exiting the loop.
print('Disconnected from server')
