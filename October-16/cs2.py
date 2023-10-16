from functools import lru_cache
import os


@lru_cache
def readFile(file):
    with open(file, encoding='utf-8') as file:
        return file.read()

print(readFile('./input.txt'))
os.remove('./input.txt')
print(readFile('./input.txt'))