print("Enter your coordinates below!")
user_in_x1 = input("Enter your first x: ")
user_in_x2 = input("Enter your second x: ")
user_in_y1 = input("Enter your first y: ")
user_in_y2 = input("Enter your second y: ")
try:
    x1 = int(user_in_x1)
    x2 = int(user_in_x2)
    y1 = int(user_in_y1)
    y2 = int(user_in_y2)
except ValueError as err:
    print("Incorrect data: ", err)
else:
    length = (y2-y1) ** 2 + (x2 - x1) ** 2 
    length_cont = length ** 0.5
    print("Your length between two points is: ", length_cont)
