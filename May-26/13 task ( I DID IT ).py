print("This programm will show you the length of the side of the shape that you want")
user_in_diam = input("Enter the diameter of the circumscribed circle: ")
user_in_sides = input("Enter the quantity of the sides: ")
try:
    diam = int(user_in_diam)
    sides = int(user_in_sides)
except ValueError as err:
    message = ("Incorrect data", err)
else:
    formula = diam * (3.14 / sides)
    form = ("Your length of the side is %.2f")
    message = form % formula
print(message)
