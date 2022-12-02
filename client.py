import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))


messege = client.recv(1024).decode()
client.send(input(messege).encode())

messege = client.recv(1024).decode()
client.send(input(messege).encode())
print(client.recv(1024).decode())
