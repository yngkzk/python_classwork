from client import XoClient
from server import XoServer
from model import XoModel
from view import XoViev


class XoApplication:
    port = 10101
    def __init__(self, size, mode='client', hostname='localhost', char=''):
        if mode == 'server':
            if char in ('X', 'O'):
                self.char = char
            else:
                raise RuntimeError(f"Char must be specified: 'X' or 'O'")
            self.connector = XoServer(hostname, self.port)
        elif mode == 'client':
            self.char = ''
            self.connector = XoClient(hostname, self.port)
        else:
            raise RuntimeError(f"Unknown mode: '{mode}'")
        
        self.model = XoModel(size)
        self.view = XoViev()
        self.connector.on_char_request = self.other_char


    def other_char(self):
        return 'X' if self.char == 'O' else 'O'


    def start(self):
        if not self.char:
            self.char = self.connector.char_request()
            self.view.show(str(self.model))
            self.my_turn()
        while True:
            self.opponent_turn()
            if self.check_win(self.other_char()):
                self.view.show_loose()
                break
            self.my_turn()
            if self.check_win(self.char):
                self.view.show_win()
                break
        

    def my_turn(self):
        turn_done = False
        while not turn_done:
            row, col = self.view.input(self.char)
            if self.model.is_empty(row, col):
                turn_done = True
            else:
                print('Cell is already occupied!')
        self.model.set(row, col, self.char)
        self.connector.send(row, col)
        self.view.show(str(self.model))
    

    def opponent_turn(self):
        row, col = self.connector.receive()
        self.model.set(row, col, self.other_char())
        self.view.show(str(self.model))
    

    def check_win(self, char):
        win_row = char * self.model.size
        win_list = []
        for i in range(self.model.size):
            win_list.append(''.join(self.model.row(i)))
            win_list.append(''.join(self.model.col(i)))
        win_list.append(''.join(self.model.diag(1)))
        win_list.append(''.join(self.model.diag(-1)))
        return win_row in win_list