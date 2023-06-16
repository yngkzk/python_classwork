from ticket import Ticket

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
    