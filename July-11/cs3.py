my_file = open('input3.txt', encoding='utf-8')
text = my_file.read()
my_file.close()

splitted =  text.split()

def check_digit(word):
    if word.isdigit():
        return True

text = list(filter(check_digit, splitted))

print(text)