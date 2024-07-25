from pygame import Surface, draw
from src.library.object.object import Object
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector
from src.library.pygame.keys import Keys
from src.library.constants.game_config_constants import GameConfigConstants
import pygame


class Bullet(Object):

    def __init__(self, screen: Surface, position: Vector) -> None:
        super().__init__()
        self.game_config_constants = GameConfigConstants()
        self.pygame_engine = PygameEngine()
        self._screen: Surface = screen
        self._position = self.pygame_engine.default_position(position.x, position.y)
        self.size = [10, 10]
        self.pixel_to_meters = 20
        self.bullet_speed_default = 40
        self.color = pygame.Color('white')

    def move_object(self, delta_time: float) -> None:
        move_amount = self.bullet_speed_default * delta_time
        new_y = self._position.y - move_amount
        self._position.y = new_y
        if self._position.y + self.size[1] < 0:
            self.destroy()
                
    def draw_object(self) -> None:
        draw.rect(self._screen, self.color, (self._position.x * self.pixel_to_meters + 35, self._position.y * self.pixel_to_meters, self.size[0], self.size[1]))
