my_file = open('input5.txt', encoding='utf-8')
text = my_file.read()
my_file.close


user_in = input('Letter: ')

def firstAndLast(letter, st):
    first_index = st.find(letter)
    reversed_st = st[::-1]
    index = reversed_st.find(letter)
    lenght = len(st)
    second_index = lenght - index
    return [first_index, second_index]

result = firstAndLast(user_in, text)
print(result)

