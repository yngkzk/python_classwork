from model import XoModel



class XoViev:
    letters = 'abcdefg'

    def show(self, string):
        print(string)

    def show_win(self):
        print('You win! Congrats!')
        return

    def show_loose(self):
        print('Unlucko, u lost :(')
        return 

    def input(self, char):
        user_in = input(f'Now its {char} turn: ')
        col = self.letters.index(user_in[0])
        row = user_in[1]
        return int(row)-1, col





#     Класс содержит методы, позволяющие:
# • отобразить любой текст (show);
# • отобразить сообщение о выигрыше (show_win);
# • отобразить сообщение о проигрыше (show_loose);
# • сообщить пользователю какой мастью он играет и принять его очередной ход (input).


if __name__ == '__main__':
    pass