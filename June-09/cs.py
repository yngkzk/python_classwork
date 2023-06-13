num = 1

if num < 10:
    print("Less.")
else:
    print("More or equal.")

while num < 10:
    num += 1
    if num == 5:
        continue
    print("Less. ", num)
else:
    print("More or equal.")

print("End.")