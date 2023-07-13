import socket

def vpn_server():
    server_host = '0.0.0.0'
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)

    print(f'VPN server is listening on {server_host}:{server_port}')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'New connection from {client_address[0]}:{client_address[1]}')

        # Handle client requests and send/receive data

        client_socket.close()

if __name__ == '__main__':
    vpn_server()
