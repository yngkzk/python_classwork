user_in_dis = input("What is distance between two cities (in miles)? ")
user_in_hours = input("What time do you want to spend to travel? ")
try:
    dis = int(user_in_dis)
    hours = int(user_in_hours)
except ValueError:
    message = "Incorrect data"
else: 
    formula = dis / hours
    form = "You have to move with that speed: %.2f m/h"
    message = form % formula
print(message)