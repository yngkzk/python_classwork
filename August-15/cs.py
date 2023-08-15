# BigO

user_in = input('Enter numbers with ",": ')
my_list = user_in.split(',')

my_list = list(map(int, my_list))


is_sorted = False
while not is_sorted:
    is_sorted = True
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            is_sorted = False
        else:
            continue

print(my_list)
