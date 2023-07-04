my_file = open("text.txt", encoding="utf-8")
# text = my_file.read()
text = my_file.read()
my_file.close()

user_in_old = input("Enter old word that u want to replace: ")
user_in_new = input("Enter new word that u want to put: ")

text = text.replace(user_in_old.upper(), user_in_new.upper())
text = text.replace(user_in_old.lower(), user_in_new.lower())
text = text.replace(user_in_old.capitalize(), user_in_new.capitalize())

print(text)
