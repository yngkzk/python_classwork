my_list = ['f', 'g', 54, -1, 'h', 0, True, 'A', '$', 'Z', 13, 'm']


def get_integer(element):
    if type(element) is int:
        return True
    else:
        return False

def get_letter(element):
    if type(element) is str:
        return True
    else:
        return False

def get_upper_letter(element):
    if type(element) is str:
        if element.isupper():
            return True
        else:
            return False
    else:
        return False

first_list = list(filter(get_upper_letter, my_list))
second_list = list(filter(get_integer, my_list))
third_list = list(filter(get_letter, my_list))
print(first_list, second_list, third_list)