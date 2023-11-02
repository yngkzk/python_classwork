import pygame
from controllable import Controllable
from collider import Collider
from physicbody import PhysicBody
from world import World

class Block(Controllable):
    other_objects: list
    SPEED = 5
    static = None

    def __init__(self, size, color, controllable = False, mass = 0):
        self.controllable = controllable
        self.size = size
        self.color = color
        self.mass = mass
        self.position = [0,0]
        super().__init__()
        self.body = pygame.Surface(size)
        self.body.fill(self.color)
        self.collider = Collider(self.position, self.size)
        self.world = World((0, 10), (0, 0), 25)
        self.physicBody = PhysicBody(self.world, 50)
        
    def set_object_list(self, other_objects):
        self.other_objects = other_objects

    def default_controls(self):
        if self.controllable:
            return (
                {"key": pygame.K_w, "action": self.moveUp},
                {"key": pygame.K_a, "action": self.moveLeft},
                {"key": pygame.K_d, "action": self.moveRight},
                {"key": pygame.K_s, "action": self.moveDown}
            )     
        else:
            return ()


    def set_position(self, position):
        # self.hide()
        collision = False
        old_position = self.position
        self.collider.set_position(position)
        for other in self.other_objects:
            if other is not self:
                collision |= self.collider.check_collision(other.collider)
        if not collision: 
            self.position = position
        else:
            self.collider.set_position(old_position)
        # self.show()

    def update(self):
        # self.position = self.physicBody.position() 
        # Не понял как выполнить этот метод
        self.check_controls()

    def moveUp(self):
        #TODO: поменять на вызов метода set_position
        self.set_position((self.position[0], self.position[1] - self.SPEED))
    
    def moveDown(self):
        self.set_position((self.position[0], self.position[1] + self.SPEED))

    def moveLeft(self):
        self.set_position((self.position[0] - self.SPEED, self.position[1]))

    def moveRight(self):
        self.set_position((self.position[0] + self.SPEED, self.position[1]))
    
    def show(self):
        self.owner.blit(self.body, self.position)

    def hide(self):
        pass # Не знаю как реализовать этот метод
    
    def placeTo(self, owner):
        self.owner = owner

        

    