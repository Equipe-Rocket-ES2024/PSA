from pygame import Surface
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector


class Background:
    def __init__(self, image_path: str, speed: Vector, screen: Surface):
        self.pygame_engine = PygameEngine()
        self.image = self.pygame_engine.load_sprite_image(image_path).convert()
        self.image = self.pygame_engine.scale_sprite(self.image, screen.get_width(), screen.get_height())
        self.speed = speed
        self.y_pos = 0
        self.screen = screen

    def paralax(self):
        self.y_pos += self.speed.y
        if self.y_pos >= self.screen.get_height():
            self.y_pos = 0

    def draw(self):
        self.screen.blit(
            self.image, 
            (0, self.y_pos)
        )
        self.screen.blit(
            self.image, 
            (0, self.y_pos - self.screen.get_height())
        )
        
        if self.y_pos < 0:
            self.screen.blit(self.image, (0, self.y_pos - self.screen.get_height()))