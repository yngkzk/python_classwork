my_list = ['программирование', 'питон', 'сократил', 'слово']

def cut_word(word):
    first_2 = word[:2]
    last_2 = word[-2:]
    return first_2 + '-' + last_2

map_list = list(map(cut_word, my_list))
print(map_list)