class World: 
    def __init__(self, gravity, velocity, fps): 
        self.gravity = gravity
        self.velocity = velocity
        self.time = 1 / fps
