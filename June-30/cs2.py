my_numbers = [1,2,4,61,7,8,2,54,2,4,1,2,-1,-123,-12,-12,8,0]


def true_or_false(num):
    if num > 0:
        return True
    if num <= 0:
        return False


my_list = map(true_or_false, my_numbers)
print(list(my_list))