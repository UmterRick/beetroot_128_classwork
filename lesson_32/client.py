import socket


def start_client_udp(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        message = input("Message: ")
        client_socket.sendto(message.encode(), (host, port))
        response, server_addr = client_socket.recvfrom(1024)
        print(f"Echo from server: {response.decode()}")

def start_client_tcp(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = input("Message: ")
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024)
        print(f"Echo from server: {response.decode()}")


if __name__ == "__main__":
    start_client_tcp("127.0.0.1", 65432)
