print("This program shows if your number has the same digits")
user_in = input("Enter there your a 3-digit number: ")
try:
    user_in = int(user_in)
    un = user_in
    d1 = user_in // 100
    d2 = user_in % 100 // 10
    d3 = user_in % 10
except ValueError:
    msg = "Incorrect data, you have to enter a 3-digit number!"
except NameError as Nerr:
    msg = "Incorrect data: " + Nerr + ". You have to enter a 3-digit number!"
if user_in == str(user_in):
    msg = "Incorrect data: " + user_in + ". You have to enter a 3-digit number!"
elif d1 == d2 and d1 == d3:
    msg = "You have 3 same digits"
elif d1 != d2 and d2 == d3: 
    msg = "You have 2 same digits"
elif d1 != d3 and d2 == d1:
    msg = "You have 2 same digits"
elif d2 != d3 and d1 == d3:
    msg = "You have 2 same digits"
elif d1 != d2 and d1 != d3:
    msg = "All digits are different"
else:
    msg = "Result."
print(msg)