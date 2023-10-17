def my_generator(max_limit):
    current = 1
    while current <= max_limit:
        yield current
        current += 1

for item in my_generator(5):
    print(item)

def printer():
    yield 'Hello'
    yield 'Howru'
    yield 'Bye'
    yield 'seeya'

it = printer()
print(next(it))

newIt = printer()
result = tuple(map(lambda x: x.upper(), newIt))
print(result)