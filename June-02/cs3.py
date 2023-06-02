def factor(num):
    if num == 1:
        return 1
    if num < 0:
        print("Incorrect data.")
        return
    return num * factor(num-1)

result = factor(-6)
print(result)