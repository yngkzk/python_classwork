my_file = open('input4.txt', encoding='utf-8')
text = my_file.read()
my_file.close()


new_text = ' '
for i in range(len(text)):
    last_letter = new_text[-1]
    if text[i] == last_letter:
        new_text = new_text[:-1]
        new_text += text[i]
    else:
        new_text += text[i]


print(new_text)