text = input("Enter the 3 letter word: ")
first_char = text[0]
second_char = text[1]
third_char = text[2]

try:
    first_code = ord(first_char)
    second_code = ord(second_char)
    third_code = ord(third_char)
except IndexError as err:
    print("Incorrect data", err)
else:
    code_sum = first_code + second_code + third_code

print("Your sum of the symbols code is: ", code_sum)