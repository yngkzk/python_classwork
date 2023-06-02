def remainder(a, b):
    if a and b == 0:
        return 1
    quotient = a // b  
    product = quotient * b  
    remainder = a - product  
    return remainder

mod = remainder(13, 6)
print(mod)