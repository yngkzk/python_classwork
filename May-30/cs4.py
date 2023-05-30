print("This program shows where is your point depend on the coordinates.")
user_in1 = input("Enter there your coordinates for X: ")
user_in2 = input("Enter there your coordinates for Y: ")
x = float(user_in1)
y = float(user_in2)
if x > 0 and y > 0:
    print("Your point is in the 1st quarter")
elif x < 0 and y > 0:
    print("Your point is in the 2st quarter")
elif x < 0 and y < 0:
    print("Your point is in the 3st quarter")
elif x > 0 and y < 0:
    print("Your point is in the 4st quarter")
elif x == 0:
    print("Your point is on the X-axis")
elif y == 0:
    print("Your point is on the Y-axis")
elif x == 0 and y == 0:
    print("Your point is on the zero-point")
else:
    print("Incorrect data")
print("Here is your result.")