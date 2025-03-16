# Design Explanation: Secure TCP Client-Server Model

## 1. Client-Server Communication

This program implements a **TCP-based client-server model** with secure encrypted communication. The interaction follows these steps:

1. **Server Startup**: The server starts listening on a specified port for incoming client connections.
2. **Client Connection**: A client establishes a connection with the server.
3. **Secure Message Exchange**:
   - The client encrypts a message using **AES-256-CBC** and sends it to the server.
   - The server decrypts the received message and logs it.
   - The server sends an **encrypted acknowledgment** back to the client.
   - The client decrypts and displays the acknowledgment.
4. **Multiple Clients**: The server can handle multiple clients concurrently using **multi-threading**.

---

## 2. Multi-Threading Model

The server is designed to handle **multiple client connections concurrently** using **multi-threading**. 

- When a client connects, the server creates a **new thread** to handle communication with that specific client.
- This allows multiple clients to interact with the server **simultaneously** without blocking other connections.
- The threading model ensures efficient use of system resources and responsiveness.

### **Threading Implementation**
- **Main thread**: Listens for incoming connections.
- **Client threads**: Each new client connection is assigned a separate thread using Python’s `threading` module.

---

## 3. Encryption Implementation

### **AES-256 Encryption (CBC Mode)**
This program uses **AES-256-CBC** (Cipher Block Chaining mode) for encrypting and decrypting messages. The encryption process ensures **confidentiality** and prevents **man-in-the-middle attacks**.

### **How Encryption Works**
- A **32-byte encryption key** is used for AES-256.
- A **16-byte Initialization Vector (IV)** is randomly generated for each message.
- Messages are **padded** to fit AES block size before encryption.
- The **IV is prepended** to the ciphertext so that the recipient can properly decrypt the message.
- The same key must be used by both the **client and server** for encryption and decryption.

### **Encryption Process**
1. Generate a **random IV**.
2. Encrypt the plaintext message using **AES-256-CBC**.
3. Prepend the IV to the ciphertext.
4. Send the encrypted message over the network.

### **Decryption Process**
1. Extract the **IV** from the received ciphertext.
2. Decrypt the message using **AES-256-CBC**.
3. Remove the padding to get the original plaintext.

---
