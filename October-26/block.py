import pygame
from controllable import Controllable
from collider import Collider

class Block(Controllable):
    other_objects: list
    SPEED = 5

    def __init__(self, size, color, controllable = False):
        self.controllable = controllable
        self.size = size
        self.color = color
        self.position = [0,0]
        super().__init__()
        self.body = pygame.Surface(size)
        self.body.fill(self.color)
        self.collider = Collider(self.position, self.size)
        
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
                collision |= self.collider.checkCollision(other.collider)
        if not collision: 
            self.position = position
        else:
            self.collider.set_position(old_position)
        # self.show()


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
    
    def placeTo(self, owner):
        self.owner = owner

        

    