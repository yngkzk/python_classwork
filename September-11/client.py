import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.110.119', 9900)

is_running = True
while is_running:
    message = input('MSG: ')
    my_socket.sendto(message.encode(), server_address)
    if message == 'exit':
        is_running = False
