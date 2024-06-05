import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
            else:
                break
        except:
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Main function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    print("Connected to the server")

    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    send_messages(client_socket)

start_client()


