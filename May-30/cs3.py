user_in = input("Enter your number: ")
num = float(user_in)
if num > 0:
    message = "This number is positive"
elif num == 0:
    message = "This number is equal to zero"
else:
    message = "This number is negative"
print("Here is your result.")
print(message)