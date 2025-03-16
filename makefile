# Python Interpreter
PYTHON = python3

# Files
SERVER = server.py
CLIENT = client.py
CRYPTO = crypto_utils.py

# Run the server
run-server:
	$(PYTHON) $(SERVER)

# Run the client
run-client:
	$(PYTHON) $(CLIENT)

# Clean logs
clean:
	rm -f server.log
