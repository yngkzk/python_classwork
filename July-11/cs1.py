my_file = open('input1.txt', encoding='utf-8')
text = my_file.readlines()
my_file.close()

new_text = ''

for i in range(len(text)):
    text[i].strip('\n')
    if text[i].startswith('abc'):
        new_text += 'www.' + text[i][3:]
    else:
        new_text += text[i] + '.com'


print(new_text)