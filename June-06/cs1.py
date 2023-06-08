import random

def get_random_int(min, max):
    diap = max - min
    result = random.random() * diap + min
    return round(result)
#num = random.random()

num = get_random_int(10, 21)
print(num)