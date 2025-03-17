from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# AES-256 requires a 32-byte key
KEY = b'ThisIsA32ByteKeyForAES-256!!!!!!'  # Ensure exactly 32 bytes

def encrypt(plaintext):
    # Encrypts the plaintext using AES-256 CBC mode with a random IV."""
    iv = os.urandom(16)  # Generate a random IV
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return iv + ciphertext  # Prepend IV for decryption

def decrypt(ciphertext):
    # Decrypts the ciphertext using AES-256 CBC mode."""
    iv = ciphertext[:16]  # Extract IV from the message
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)
    return plaintext.decode()

# Test encryption & decryption
if __name__ == "__main__":
    message = "Hello, Secure World!"
    encrypted = encrypt(message)
    decrypted = decrypt(encrypted)
    print(f"Original: {message}")
    print(f"Encrypted (hex): {encrypted.hex()}")
    print(f"Decrypted: {decrypted}")
