user_in_cap = input("Enter the capacity of your flash drive (gb): ")
user_in_file = input("Enter the capacity of your file (mb): ")
mbfile = 1024
try:
    space = int(user_in_cap)
    files_cap = int(user_in_file)
except ValueError:
    message = "Incorrect data"
else:
    flashdrive_in_gb = space * mbfile
    copy = flashdrive_in_gb // files_cap
    form = "You can copy this file %d times in your flash drive"
    message = form % copy
print(message)