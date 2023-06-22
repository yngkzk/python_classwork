from random import randint


class Person:
    balance = 0
    name = ""
    iin = 0
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.iin = randint(100000000000, 999999999999)

    def show(self):
        msg = "Passenger %s, age: %s, IIN: %s. Value: %s" % (self.name,
                                                             self.age, self.iin, self.balance)
        print(msg)

    def earn(self, amount):
        self.balance += amount

    def pay(self, amount):
        if self.balance < amount:
            return 0
        self.balance -= amount
        return amount


print("This is a person!", __name__)
