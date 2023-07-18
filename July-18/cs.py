class House:
    def __init__(self, floors, color, rooms, bathrooms):
        self.__floors = floors
        self.color = color
        self.__rooms = rooms
        self.__bathrooms = bathrooms

    def __repr__(self):
        info = 'floors - %s\n' \
               'color - %s\n' \
               'rooms - %s\n' \
               'bathrooms - %s' % (self.__floors, self.__color,
                                   self.__rooms, self.__bathrooms)
        return info


class HouseWithBalcony(House):
    def __init__(self, floors, color, rooms, bathrooms, balconies):
        super().__init__(floors, color, rooms, bathrooms)
        self.__balconies = balconies

    def __repr__(self):
        info = super().__repr__()
        return info + f'\nbalconies - {self.__balconies}'


my_house = HouseWithBalcony(2, 'red', 4, 1, 2)
print(my_house)
