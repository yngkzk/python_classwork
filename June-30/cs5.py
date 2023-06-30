from functools import reduce

num = 5

num_factor = reduce(lambda acc, x: acc*x, range(1, num+1))

print(num_factor)