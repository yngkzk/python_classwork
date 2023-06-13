task = '2 + 2 * 2' 
print(task, "you have to solve this equation.")
num = input("Enter the number: ")

while int(num) != 6:
    print("Incorrect number.")
    break
while int(num) == 6:
    print("Correct!")
    break
