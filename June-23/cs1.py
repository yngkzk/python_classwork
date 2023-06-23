user_in = input("Enter a number with ',' divider: ")
user_list = user_in.split(',')

'''
numbers = []

for x in user_list:
    numbers.append(int(x))

print(user_list)
print(numbers)
'''


def get_last_digit(num):
    return num % 10


print(user_list)

try:
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
except ValueError:
    message = 'You have to enter a number!'
else:
    end_list = sorted(user_list, key=get_last_digit, reverse=True)
    # for i in range(len(end_list)):
    #     end_list[i] = str(end_list[i])
    another_list = [str(x) for x in end_list]
    message = " - ".join(end_list)
print(message)
