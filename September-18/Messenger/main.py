import sys
from PyQt6.QtWidgets import QApplication
from router import Router


if __name__ == '__main__':
    router = Router()
    router.start()

    app = QApplication(sys.argv)
    app.exec()

