from world import World

class PhysicBody:
    velocity = [0,0]
    def __init__(self, world: World, mass, position = (0, 0)): 
        self.world = world 
        self.mass = mass
        self.position = position
        self.velocity[0] += self.world.velocity[0]
        self.velocity[1] += self.world.velocity[1]

    def set_position(self, new_position):
        self.position = new_position
    
    def update(self):
        a_x = self.world.gravity[0] / self.mass
        a_y = self.world.gravity[1] / self.mass

        self.velocity[0] += a_x * self.world.time
        self.velocity[1] += a_y * self.world.time

        new_x = self.position[0] + self.velocity[0] * self.world.time
        new_y = self.position[1] + self.velocity[1] * self.world.time

        return (new_x, new_y)


    