import pygame
from animatedsprite import AnimatedSprite
from block import Block

class Application():
    FPS = 25
    icon = 'resources/pygamelogo.png'
    background_color = (60, 60, 60)
    objects = []

    def __init__(self, size, title):
        self.size = size
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        image = pygame.image.load(self.icon)
        pygame.display.set_icon(image)
        self.player = AnimatedSprite(1.2, 'resources/sprites/anime_boy', 12, controllable=True)
        self.player.placeTo(self.screen)

        ground = Block((800, 50), 'green')
        ground.set_object_list(self.objects)
        ground.placeTo(self.screen)
        ground.set_position((0, 550))

        b = Block((50, 100), 'green')
        b.set_object_list(self.objects)
        b.placeTo(self.screen)
        b.set_position((450, 450))

        self.player.set_object_list(self.objects)
        self.objects.append(self.player)
        self.objects.append(b)
        self.objects.append(ground)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            for n in self.objects:
                n.update()
            self.screen.fill(self.background_color)
            for n in self.objects:
                n.show()

            pygame.display.update()
            clock.tick(self.FPS)
        pygame.quit()