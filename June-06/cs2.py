import random

def get_random_int(min, max):
    diap = max - min
    result = random.random() * diap + min
    return round(result)
def game(my_random, min, max):
    user_in = input("Guess a number from %s to %s: " % (min, max))
    try:
        user_in = int(user_in)
    except ValueError:
        print("You have to enter number.")
        game(num, min, max)
    else:
        if int(my_random) < int(user_in):
            print("Less.")
            game(num, min, max)
        elif int(my_random) > int(user_in):
            print("More.")
            game(num, min, max)
        else:
            print("Congratulations!")
            return
        return "Result."

num = get_random_int(0, 20)
game(num, 0, 20)