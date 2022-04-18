import socket
import requests

IP = "127.0.0.1"
PORT = 5053

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen()


def check_black_list(request):
    with open('BlackList.txt') as file:
        contents = file.read()
    if request in contents:
        return 1
    else:
        return 0


def server_dns(request):
    with open('DnsServer.txt') as file:
        lines = file.readlines()
    result = list()
    for line in lines:
        if request in line:
            result.append(line.split(' ')[1][:-1])
    return result[0]


def open_socket():
    while True:
        client, address = server.accept()

        client_date = client.recv(1024).decode('UTF-8')

        is_black_list = check_black_list(client_date)

        if is_black_list == 1:
            client.send("Your domain name in BlackList".encode('UTF-8'))
            client.close()
            return 1

        request_ip = server_dns(client_date)
        server_answer = requests.get('http://' + request_ip)

        if server_answer.status_code == 200:
            client.send("All good client!".encode('UTF-8'))
            client.close()
            return 0
        else:
            client.send("All bad client!".encode('UTF-8'))
            client.close()
            return 1


if __name__ == "__main__":
    open_socket()
