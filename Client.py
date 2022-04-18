import socket

IP = "192.168.0.1"
PORT = 8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5053))

clientRequest = input()
client.send(clientRequest.encode('UTF-8'))

date = client.recv(1024).decode('UTF-8')
print(date)