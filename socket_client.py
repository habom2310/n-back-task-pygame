import socket
import json

with open("socket_config.json") as f:
    config = json.load(f)

HOST = config.get("HOST")
PORT = config.get("PORT")

def send(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(data)
        response = sock.recv(1024)
        print(response.decode())
