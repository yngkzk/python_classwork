

class Collider():
    def __init__(self, position, size):
        self.x = position[0]
        self.y = position[1]
        self.width = size[0]
        self.height = size[1]
        print(f'newCollider w - {self.width} h - {self.height}')
    
    def check_collision(self, other):
        if other.x > self.x:
            result_x = (other.x - self.x) < self.width
        else:
            result_x = (self.x - other.x) < other.width
        if other.y > self.y:
            result_y = (other.y - self.y) < self.height
        else:
            result_y = (self.y - other.y) < other.height

        return result_x and result_y
    
    def set_position(self, new_position):
        self.x = new_position[0]
        self.y = new_position[1]
