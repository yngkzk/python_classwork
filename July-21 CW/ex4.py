# Два слова похожи, если отличаются только одной буквой. Функция проверяет, похожи строки, или нет.
def is_similar(word1, word2=None):
    if word2 is None:
        return False
    else:
        allowed = 0
        word1 = list(word1)
        word2 = list(word2)
        if len(word2) > len(word1):   # Problem
            word1.insert(0, '')
        for x in range(len(word1)):
            if word1[x] == word2[x]:
                continue
            else:
                allowed += 1
        if allowed > 1:
            return False
        else:
            return True

def test_is_similar():
    assert is_similar('пень', 'лень') == True
    assert is_similar('вторник', 'вторнек') == True
    assert is_similar('город', 'огород') == True
    assert is_similar('перец', 'конец') == False
    assert is_similar('вор', 'ворон') == False
    assert is_similar('перец') == False

test_is_similar()
