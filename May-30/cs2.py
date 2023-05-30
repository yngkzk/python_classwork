user_in = input("Enter your cost: ")
cost = int(user_in)
if cost < 1500:
    print("No discount.")
elif cost < 2000:
    print("Discount 2%.")
elif cost < 5000:
    print("Discount 5%.")
else:
    print("Discount 10%.")
print("The end.")