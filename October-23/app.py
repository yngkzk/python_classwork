import pygame
from controllable import Controllable
from block import Block


class Application:
    background_color = (60, 100, 100)
    player = None
    FPS = 25

    def __init__(self, size, title):
        self.size = size
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.player = Block((50, 50), 'yellow')


    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.player.checkBinds()
            self.screen.fill(self.background_color)
            self.player.show()
            self.screen.blit(self.player.obj, self.player.position)
            pygame.display.update()
            clock.tick(self.FPS)
        pygame.quit()