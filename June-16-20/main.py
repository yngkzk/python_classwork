from kassa import Kassa
from person import Person
from train import Train

if __name__ == "__main__":
    print("Main program", __name__)

    ilon = Person("Ilon Mask", 55)
    ilon.earn(97000)
    ilon.pay(11111)
    ilon.show()

    almaty1 = Kassa()
    price = almaty1.get_price("Almaty", "Osh")
    almaty1.buy_ticket("Almaty", "Santiago", ilon)
    almaty1.buy_ticket("Osh", "Bishkek", ilon)
    almaty1.buy_ticket("Astana", "Kolkata", ilon)

    train = Train(almaty1, "Almaty", "Santiago")
    train.show()

    print(almaty1.tickets)
    train.board(ilon)
    print(almaty1.tickets)
