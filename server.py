import socket
import threading

# Define the host and port on which the server will listen
HOST = '127.0.0.1'
PORT = 65432


# Function to handle each client connection
def handle_client(conn, addr):
    """
    Handles a client connection.

    :param conn: The connection socket object.
    :param addr: The address of the client.
    :return: None

    This function handles a client connection by printing the address of the client, receiving data from the client, printing the received data, preparing a response, and sending the response back to the client.
    """
    print(f'New connection from {addr}')
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                print(f'Connection closed by {addr}')
                break
            print(f'Received from {addr}: {data.decode()}')
            response = f'Server received: {data.decode()}'
            conn.sendall(response.encode())


# Create a socket object with IPv4 and TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f'Server listening on {HOST}:{PORT}')

    while True:
        # Accept a new connection
        conn, addr = server_socket.accept()
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
