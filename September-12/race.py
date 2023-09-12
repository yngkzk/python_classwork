import threading

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lock = threading.Lock()


def my_func():
    global numbers
    for x in range(100):
        lock.acquire()
        for i in range(len(numbers)):
            if i == len(numbers) - 1:
                numbers[i] += numbers[i] - numbers[i-1] + 1
            else:
                numbers[i] += numbers[i+1] - numbers[i]
        lock.release()


thread_1 = threading.Thread(target=my_func)
thread_2 = threading.Thread(target=my_func)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
print(numbers)
