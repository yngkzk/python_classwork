import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_address = ('localhost', 9900)
my_socket.bind(my_address)

is_running = True

while is_running:
    data, addr = my_socket.recvfrom(1024)
    print(f'Получено сообщение от {addr}: {data.decode()}')
    if data.decode() == 'exit':
        print('Работа прекращена')
        is_running = False
