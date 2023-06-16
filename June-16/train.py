from random import randint

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