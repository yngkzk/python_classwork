from app import XoApplication
import sys


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) > 2:
        if sys.argv[1] in ('server', 'client') and sys.argv[2] in ('O', 'X'):
            if len(sys.argv) > 3:
                if sys.argv[3]:
                    app = XoApplication(3, sys.argv[1], sys.argv[3], sys.argv[2])
            else:
                app = XoApplication(3, sys.argv[1], 'localhost', sys.argv[2])
    app.start()