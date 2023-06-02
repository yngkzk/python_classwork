import time

def simplerecur(num):
    time.sleep(1)
    if num < 0:
        return
    print(num)
    simplerecur(num-1)
    print(num)
simplerecur(4)