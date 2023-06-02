def simplefun(user_in1, user_in2):
    if user_in1 and user_in2 == 0:
        return 1
    return (user_in2) - (user_in1 // user_in2)
mod = simplefun(13, 7)
print(mod)