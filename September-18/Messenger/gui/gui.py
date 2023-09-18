from PyQt6.QtCore import QThread


class Gui(QThread):
    def run(self):
        print('GUI has been launched!\n')
