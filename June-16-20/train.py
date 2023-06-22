from random import randint


class Train:
    source = ""
    destination = ""
    number = 0
    kassa = None

    def __init__(self, kassa, source, destination):
        self.kassa = kassa
        self.source = source
        self.destination = destination
        self.number = randint(100, 999)
        kassa.register_train(self)

    def board(self, person):
        ticket = self.kassa.get_ticket(person.iin, self.source, self.destination)
        if ticket:
            message = "Welcome %s, your train N%s has arrived, from %s to %s." % (person.name,
                                                                                  self.number, self.source,
                                                                                  self.destination)
            print(message)
            self.kassa.delete_ticket(ticket)
        else:
            print("You have not ticket")

    def show(self):
        message = "Train N%s, from station %s to station %s." % (self.number,
                                                                 self.source, self.destination)
        print(message)


print("This is a train!", __name__)
