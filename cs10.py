three_digit_number = input("Enter three digit number: ")
try:
    tdn = int(three_digit_number)
    n1 = tdn // 100
    n2 = tdn % 100 // 10
    n3 = tdn % 10
except ValueError:
    print("Incorrect data") 
else:
    sn1 = str(n1)
    sn2 = str(n2)
    sn3 = str(n3)
    print(sn3, sn2, sn1, sep="")
