my_file = open('input2.txt', encoding='utf-8')
text = my_file.read()
my_file.close()

cut_text = text.split()
word_len = float('inf')

for i in range(len(cut_text)):
    if len(cut_text[i]) < word_len:
        word_len = len(cut_text[i])

print(word_len)