# Функция возвращает список array в перевернутом виде, но только из тех элементов, которые не превышают значение max.
def reverse_limited(array, max=None):
    if max is None:
        return array[::-1]
    else:
        reverse = array[::-1]
        new_list = list(filter((lambda x: True if x <= max else False), reverse))
        return new_list


def test_reverse_limited():
    input  = [21,9,6,11,4,15]
    max = 11
    expect = [4,11,6,9]
    assert reverse_limited(input, max) == expect

    input  = [3,19,16,14,5]
    max = 2
    expect = []
    assert reverse_limited(input, max) == expect

    assert reverse_limited(input) == input[::-1]

test_reverse_limited()
