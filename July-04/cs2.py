my_file = open("text.txt", encoding="utf-8")
# text = my_file.read()
text = my_file.read()
my_file.close()

palindrome = filter(lambda x: x == x[::-1] and len(x) > 2, text.lstrip().split(' '))

print(list(palindrome))
