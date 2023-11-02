import pygame
from block import Block


class StaticSprite(Block):
    def __init__(self, scale, sprite_file, controllable = False, mass = 0):
        self.controllable = controllable
        self.mass = mass
        sprite = pygame.image.load(sprite_file)
        width = sprite.get_width() * scale
        height = sprite.get_height() * scale
        self.image = pygame.transform.scale(sprite, (width, height))
        super().__init__((width, height), (0, 0, 0))
        self.body = self.image
          

    def default_controls(self):
        if self.controllable:
            return super().default_controls()
        else:
            return ()