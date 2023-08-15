user_in = input('Enter numbers with ",": ')
my_list = user_in.split(',')

my_list = list(map(int, my_list))

new_list = []

for _ in range(len(my_list)):
    # min_number = min(my_list)
    # new_list.append(min_number)
    # del my_list[my_list.index(min_number)]
    min_index = 0
    for k in range(1, len(my_list)):
        if my_list[k] < my_list[min_index]:
            min_index = k
    new_list.append(my_list[min_index])
    del my_list[min_index]
print(new_list)
