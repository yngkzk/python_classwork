text = "dsnaldsandslad nds@kalnd dks@land klsand klsadnlk sa@gmail.com"

text = text.split()


def find_email(word):
    for i in range(len(word)):
        if word[i] == '@':
            return True
    else:
        return False


text = filter(find_email, text)
print(list(text))
