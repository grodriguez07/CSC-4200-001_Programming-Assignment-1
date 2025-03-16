import socket
from crypto_utils import encrypt, decrypt

def start_client(server_host="127.0.0.1", server_port=12345):
    """Starts the TCP client."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    try:
        message = input("Enter message to send: ")
        encrypted_msg = encrypt(message)
        client.send(encrypted_msg)

        encrypted_ack = client.recv(1024)
        ack_msg = decrypt(encrypted_ack)

        print(f"Server response: {ack_msg}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
