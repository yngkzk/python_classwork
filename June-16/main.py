from kassa import Kassa
from person import Person
from ticket import Ticket
from train import Train

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