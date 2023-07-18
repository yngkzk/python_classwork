class Car:
    fuel = 0
    distance = 0

    def __init__(self, color, weight, year, bag_capacity):
        self.__color = color
        self.__weight = weight
        self.__year = year
        self.__bag_capacity = bag_capacity

    def refuel(self, litres):
        if self.fuel < self.__bag_capacity:
            self.fuel += litres
            return f'Вы заправили автомобиль на {self.fuel}'
        elif self.fuel > self.__bag_capacity:
            self.fuel += litres
            return f'Вы заправили автомобиль полностью, но пролили {self.fuel - self.__bag_capacity}'
        else:
            return 'Автомобиль заправлен'