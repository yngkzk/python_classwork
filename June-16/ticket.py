from random import randint

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
