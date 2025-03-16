# CSC-4200-001_Programming-Assignment-1
- Title: Programming Assignment 1: Basic TCP Client Server Model
- Author: Geovany Rodriguez
- Due Date: 3/16/2025

# TCP Client-Server Model

## Overview
This program implements a basic TCP client-server communication model using Python sockets with multi-threading and encryption.

## Features
- Multi-threaded TCP server that handles multiple clients.
- Secure communication using AES encryption/decryption.
- Logging of received messages.
- Client sends encrypted messages and receives acknowledgments.

## Requirements
Ensure you have Python 3 installed. Install dependencies with:

pip3 install pycryptodome

## How To Run
- Start the Server:
  make run-server
- Start the Client:
  make run-client
- Clean Up:
  make clean
## Project Structure
- server.py: Multi-threaded TCP Server
- client.py: TCP Client
- crypto_utils.py: AES-256 Encryption/Decryption Module
- Makefile: Automates build/run/clean
- README.md: Documentation
- server.log: Logs received messages (auto-generated)
- design_explanation.md: Documents server-client communication, threading, and encryption utilized in the program
