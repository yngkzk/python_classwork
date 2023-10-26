import pygame 
from block import Block 

class AnimatedSprite(Block): 

    def __init__(self, scale, sprite_dir, frames, controllable = False): 
        self.SPEED = 8
        self.frames = frames
        self.current_frame = 0 
        self.controllable = controllable
        self.sp_up = pygame.image.load(sprite_dir + '/up.png')
        self.sp_down = pygame.image.load(sprite_dir + '/down.png')
        self.sp_right = pygame.image.load(sprite_dir + '/right.png')
        self.sp_left = pygame.image.load(sprite_dir + '/left.png')
        self.width = self.sp_up.get_width() * scale
        self.height = self.sp_up.get_height() * scale
        self.frame_width = self.width / self.frames
        self.current_sprite = self.sp_up
        self.image = pygame.transform.scale(self.current_sprite, (self.width, self.height))
        super().__init__((self.frame_width, self.height), (0, 0, 0))
        self.body.set_colorkey((0, 0, 0))

    def set_current_sprite(self, sprite):
        self.current_sprite = sprite
        self.image = pygame.transform.scale(self.current_sprite, (self.width, self.height))
        self.current_frame = 0

    def show(self):
        self.body.fill((0, 0, 0))
        self.body.blit(self.image, (0, 0), (self.frame_width * self.current_frame, 0, self.frame_width, self.height))
        super().show()

    def next_frame(self):
        self.current_frame += 1
        if self.current_frame >= self.frames: 
            self.current_frame = 0        

    def moveUp(self):
        super().moveUp()
        if self.current_sprite is self.sp_up:
            self.next_frame()
        else:
            self.set_current_sprite(self.sp_up)
    
    def moveDown(self):
        super().moveDown()
        if self.current_sprite is self.sp_down:
            self.next_frame()
        else:
            self.set_current_sprite(self.sp_down)
    

    def moveLeft(self):
        super().moveLeft()
        if self.current_sprite is self.sp_left:
            self.next_frame()
        else:
            self.set_current_sprite(self.sp_left)
       

    def moveRight(self):
        super().moveRight()
        if self.current_sprite is self.sp_right:
            self.next_frame()
        else:
            self.set_current_sprite(self.sp_right)


    def default_controls(self):
        if self.controllable:
            return super().default_controls()
        else:
            return ()