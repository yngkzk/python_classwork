# Функция принимает двумерный массив, содержащий буквы, и выводит два слова, составленные из букв главной и побочной диагоналей.
def get_diag_words(array=None):
    if array:
        word = ''
        for r in range(0, len(array)):
            for c in range(0, len(array[r])):
                if r == c:
                    word += array[r][c]
        word += ' '
        for c2 in range(0, len(array)):
            index = len(array[c2]) - c2 - 1
            word += array[c2][index]
        return word
    return ''


def test_get_diag_words():
    input = [['ж','ф','л'],
             ['р','и','а'],
             ['с','з','л']]
    expect = "жил лис"
    assert get_diag_words(input) == expect

    input = [['б','ф','л','т',']','в'],
             ['р','е','а','о','о','щ'],
             ['е','и','л','р','э','к'],
             ['г','ы','о','а','ф','о'],
             ['н','н','а','а','я','ч'],
             ['а','з','л','ц','в',' ']]
    expect = "белая  ворона"
    assert get_diag_words(input) == expect

    input = []
    expect = ""
    assert get_diag_words(input) == expect


test_get_diag_words()
