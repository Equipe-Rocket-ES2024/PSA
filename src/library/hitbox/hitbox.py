from src.library.pygame.pygame import PygameEngine
import copy
from src.library.vector.vector import Vector


class Hitbox:
    
    def __init__(self, object, scale: Vector, displacement: Vector):
        self.object = object
        self.displacement = copy.copy(displacement)
        self.width = object.size[0] * scale.x
        self.height = object.size[1] * scale.y
        self.pygame_engine = PygameEngine()
        self.rect = self.pygame_engine.create_rect(
            object.position.x * object.meters_to_pixel,
            object.position.y * object.meters_to_pixel,
            self.width, 
            self.height
        )       


    def update(self):
        self.rect.x = (self.object.position.x + self.displacement.x) * self.object.meters_to_pixel
        self.rect.y = (self.object.position.y + self.displacement.y) * self.object.meters_to_pixel


    @staticmethod
    def check_collision(hitbox1, hitbox2):
        return hitbox1.rect.colliderect(hitbox2.rect)
