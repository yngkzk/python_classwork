import socket


class XoClient:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, address='localhost', port=10101):
        self.address = address
        self.port = port

    def char_request(self):
        user_in = input('Which one? (O, X): ')
        return user_in

    def send(self, row, col):
        message = f'{row}, {col}'
        self.server_socket.sendto(message.encode(), (self.address, self.port))

    def receive(self):
        data, addr = self.server_socket.recvfrom(1024)
        message = data.decode(encoding="UTF-8")
        # print('Response from the server:', data.decode(encoding='UTF-8'), sep=' ')
        print('RECEIVED', message)
        return message, message

if __name__ == '__main__':
    client = XoClient('127.0.0.1', 9900)
    client.send('b2')
    client.receive()

# Конструктор класса должен создать клиентский сокет для коммуникации с сервером, и
# принимает обязательные параметры для этого: имя хоста сервера и номер порта.
# Класс содержит методы, позволяющие:
# • отправить запрос серверу «какой мастью мне играть?» (char_request);
# • отправить серверу информацию о только что сделанном ходе (send);
# • дождаться хода сервера и получить информацию о нём, т.е. строку и столбец 
# (receive).