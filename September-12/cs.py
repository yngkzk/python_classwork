import threading
import time


my_numbers = tuple(range(50))
average_numbers = []
lock = threading.Lock()


def average(nums):
    global average_numbers
    lock.acquire()
    result = sum(nums)/len(nums)
    average_numbers.append(result)
    lock.release()
    return result


threads = 5
FROM, TO = 0, 10

for x in range(threads):
    thread = threading.Thread(target=average, args=tuple((my_numbers[FROM:TO],)))
    thread.start()
    thread.join()
    FROM += 10
    TO += 10


print(average_numbers)
