import socket


class XoServer:
    addr = None

    def __init__(self, hostname, port=10101):
        self.port = port
        self.server_address = (hostname, self.port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(self.server_address)
        self.is_enabled = True

    def char_response(self):
        pass

    def send(self, row, col):
        sender_ip, sender_port = self.addr[0], self.addr[1]
        message = f'{row}, {col}'
        self.server_socket.sendto(message.encode(), (sender_ip, sender_port))

    def receive(self):
        data, self.addr = self.server_socket.recvfrom(1024)
        message = data.decode(encoding="UTF-8")
        return tuple(map(int, message.split(', ')))


if __name__ == '__main__':
    my_server = XoServer('127.0.0.1')
    my_server.receive()

# Конструктор класса должен создать серверный UDP сокет и принимат обязательные
# параметры для этого: имя хоста и номер порта.
# Класс содержит методы, позволяющие:
# • отправить ответ на запрос масти от клиента (char_response);
# • отправить клиенту информацию о только что сделанном ходе (send);
# • дождаться хода клиента и получить информацию о нём, т.е. строку и столбец 
# (receive).