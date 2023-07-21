# Функция возвращает аббревиатуру от переданной строки
def get_abbr(phrase):
    split = phrase.split(' ')
    new_text = ''
    for i in range(len(split)):
        index = split[i]
        if len(index) > 1:
            cut = index[:1]
            new_text += cut.capitalize()
        else:
            new_text += index
    return new_text


def test_get_abbr():
    assert get_abbr('семь раз отмерь - один раз отрежь') == 'СРО-ОРО'
    assert get_abbr("don't repeat yourself") == 'DRY'
    assert get_abbr('') == ''

test_get_abbr()
