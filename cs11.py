print("Enter your coordinates below!")
user_in_x1 = input("Enter your first x: ")
x1 = int(user_in_x1)
user_in_x2 = input("Enter your second x: ")
x2 = int(user_in_x2)
user_in_y1 = input("Enter your first y: ")
y1 = int(user_in_y1)
user_in_y2 = input("Enter your second y: ")
y2 = int(user_in_y2)
length = (y2-y1) ** 2 + (x2 - x1) ** 2 
length_cont = length ** 0.5
print("Your length between two points is: ", length_cont)
