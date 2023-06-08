def is_simple(num, div=2):
    if int(num) < 2:
        return False
    if int(div) >= int(num):
         return True
    if int(num) % div == 0:
        return False
    else:
        return is_simple(num, div+1)

print(is_simple(23))