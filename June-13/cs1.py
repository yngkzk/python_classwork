class Kettle():
    material = ""
    color = ""
    volume = 2.4
    water = 0
    temperature = 20

    def __init__(self, material, color, volume):
        self.material = material
        self.color = color
        self.volume = volume

    def fill(self, liters):
        self.water += liters
        if self.volume < self.water:
            liters -= self.volume
            self.water = self.volume
            return "Dropped %.1f l of extra water" % liters
        else:
            return f"Now in kettle {self.water} l."

    def pour(self, liters):
        if self.volume > liters:
            self.water = 0
            return "It can't drop %.1f l of extra water" % liters
        else:
            return f"Now in kettle {self.water} l."    

    def boil(self):
        self.temperature = 100
        return "Wheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee!!!"
my_kettle = Kettle("steel", "red", 2.4) 
print(my_kettle.pour(2))
print(my_kettle.boil())