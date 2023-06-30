from functools import reduce


# map, filter, reduce

def sum(a, b):
    return a + b

summary = lambda a, b: a + b

# map
names = ["Евгений", "Даниил", "Руслан", "Артем", "Ансар", "Шолпан", "Глеб", "Виталий"]

def first_char(text):
    return text[0]

chars = map(lambda x: x[0], names)
print(list(chars))

# filter
big_names = filter(lambda x: len(x) > 5, names)
print(list(big_names))

# reduce
result = reduce(lambda acc, x: acc+x, names)
print(result)

chars = reduce(lambda acc, x: acc+[x[0]], names, [])
print(chars)

big_names = reduce(lambda acc, x: acc + [x] if len(x) > 5 else acc, names, [])
print(big_names)