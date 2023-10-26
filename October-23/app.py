import pygame
from animatedsprite import AnimatedSprite

class Application():
    FPS = 25
    icon = 'resources/pygamelogo.png'
    background_color = (60, 60, 60)

    def __init__(self, size, title):
        self.size = size
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        image = pygame.image.load(self.icon)
        pygame.display.set_icon(image)
        self.player = AnimatedSprite(1.2, 'resources/sprites/anime_boy/', 12, controllable=True)
        self.player.placeTo(self.screen)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            self.player.check_controls()
            self.screen.fill(self.background_color)
            self.player.show()

            pygame.display.update()
            clock.tick(self.FPS)
        pygame.quit()