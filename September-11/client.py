import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

server_address = ('255.255.255.255', 9900)

is_running = True

while is_running:
    message = input('MSG: ')
    my_socket.sendto(message.encode(), server_address)
    if message == 'exit':
        is_running = False
