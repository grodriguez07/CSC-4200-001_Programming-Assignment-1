import socket
import threading
import logging
from crypto_utils import encrypt, decrypt

logging.basicConfig(filename="server.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def handle_client(client_socket, address):
    """Handles communication with a single client."""
    try:
        while True:
            encrypted_msg = client_socket.recv(1024)
            if not encrypted_msg:
                break

            decrypted_msg = decrypt(encrypted_msg)
            logging.info(f"Received from {address}: {decrypted_msg}")

            ack_msg = f"ACK: {decrypted_msg}"
            encrypted_ack = encrypt(ack_msg)

            client_socket.send(encrypted_ack)
    except Exception as e:
        print(f"Error handling client {address}: {e}")
    finally:
        client_socket.close()

def start_server(host="0.0.0.0", port=12345):
    """Starts the TCP server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
