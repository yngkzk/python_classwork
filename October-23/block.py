import pygame
from controllable import Controllable


class Block(Controllable):
    def __init__(self, size, color):
        super().__init__()
        self.size = size
        self.color = color
        self.position = [0, 0]
        self.obj = pygame.Surface(self.position)

    def defaultBinds(self):
        return (
            {"key": pygame.K_w, "action": lambda: print(self.moveUp)},
            {"key": pygame.K_a, "action": lambda: print(self.moveLeft)},
            {"key": pygame.K_d, "action": lambda: print(self.moveRight)},
            {"key": pygame.K_s, "action": lambda: print(self.moveDown)}
        )

    def moveUp(self):
        self.position[1] -= 1

    def moveLeft(self):
        self.position[0] -= 1

    def moveRight(self):
        self.position[0] += 1

    def moveDown(self):
        self.position[1] += 1

    def show(self):
        self.obj.fill(self.color)

    def hide(self):
        pass