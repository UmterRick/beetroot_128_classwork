import  socket


def start_server_udp(host="127.0.0.1", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket: # UDP
        server_socket.bind((host, port))
        print(f"UDP Socket listening on {host}:{port}")
        while True:
            data, client_addr = server_socket.recvfrom(1024)
            print(f"receive {data} from {client_addr}")
            server_socket.sendto(f"I am server (your message was : {data.decode()} )!".encode(), client_addr)


def start_server_tcp(host="127.0.0.1", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: # UDP
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"TCP Socket listening on {host}:{port}")

        connection, addr = server_socket.accept()
        with connection:
            print(f"Connected with Client({addr})")
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                print(f"receive {data.decode()} from {addr}")
                connection.sendall(f"Server response {data.decode()}".encode())


if __name__ == "__main__":
    start_server_tcp()
