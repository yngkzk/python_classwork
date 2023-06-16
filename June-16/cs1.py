from random import randint

class Person:
    balance = 0
    name = ""
    iin = 0
    age = 0
    ticket = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.iin = randint(100000000000, 999999999999)

    def show(self):
        message = "Name - %s, age - %s y.o., IIN - %s. Value: %s" % (self.name, self.age, self.iin, self.balance)
        print(message)

    def earn(self, amount):
        self.balance += amount

    def pay(self, amount):
        if self.balance < amount:
            return 0
        self.balance -= amount
        self.ticket = True
        return amount

class Ticket:
    passenger_name = ""
    ticket_number = 0
    passenger_iin = 0
    data = 0
    source = ""
    destination = ""

    def __init__(self, source, destination, passenger_name, passenger_iin, data):
        self.ticket_number = randint(100000, 999999)
        self.passenger_name = passenger_name
        self.passenger_iin = passenger_iin
        self.source = source
        self.destination = destination
        self.data = data

    def show(self):
        message = "Dear %s, ticket N%s is ready. IIN - %s, From %s - To %s in %s" % (self.passenger_name, self.ticket_number, self.passenger_iin, self.source, self.destination, self.data)
        print(message)

class Kassa:
    balance = 0

    def get_price(self, source, destination):
        return (len(source) + len(destination)) * 1000

    def buy_ticket(self, source, destination, person):
        money = person.pay(self.get_price(source, destination))
        if money:
            self.balance += money
            person.ticket = Ticket(source, destination, person.name, person.iin, "16 hours")
        else:
            print("No money, no ticket ;)")
    
class Train:
    source = ""
    destination = ""
    number = 0

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.number = randint(10000, 99999)

    def board(self, person):
        if person.ticket:
            if self.source == person.ticket.source and self.destination == person.ticket.destination:
                message = "Welcome %s, your train N%s has arrived, from %s to %s." % (person.name, self.number, self.source, self.destination)
                print(message)
                person.ticket = None
            else:
                print("Incorrect ticket")
        else:
            print("You have not ticket")

    def show(self):
        message = "Train N%s, from %s to %s." % (self.number, self.source, self.destination)
        print(message)

test_man = Person("Ilon Flask", 55)
test_man.earn(25000)
test_man.pay(13000)
test_man.show()

test_ticket = Ticket("Almaty", "Astana", test_man.name, test_man.iin, "12.05.2024")

kassa = Kassa()
price = kassa.get_price("Almaty", "Astana")
kassa.buy_ticket("Almaty", "Astana", test_man)

if test_man.ticket:
    test_man.ticket.show()

train = Train("Almaty", "Astana")
train.show()

train.board(test_man)
if test_man.ticket is None:
    print("You have not ticket.")