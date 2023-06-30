text = "Есть произвольный текст. Оставить в тексте только пробелы и гласные буквы."

def predic(letter):
    my_list = "еоиыеау "
    if letter.lower() in my_list:
        return True
    else:
        return False

result = filter(predic, text)
print(list(result))