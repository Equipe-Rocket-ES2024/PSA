from pygame import Surface, draw
from src.library.hitbox.hitbox import Hitbox
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
        starting_x = position.x
        starting_y = position.y - self._size[1] - 1
        self._position = self.pygame_engine.default_position(starting_x, starting_y)
        self._size = [10, 10]
        self.pixel_to_meters = 20
        self.bullet_speed_default = 30
        self.color = pygame.Color('white')
        self.hitbox = Hitbox(self, self._size[0], self._size[1])

    def move_object(self) -> None:
        self._speed.y = -self.bullet_speed_default
        
    
    def physics_process(self, delta_time: float, screen_width: int, screen_height: int) -> None:
        super().physics_process(delta_time, screen_width, screen_height)
        self.hitbox.update()
        
                
    def draw_object(self) -> None:
        draw.rect(self._screen, self.color, (self._position.x * self.pixel_to_meters + 35, self._position.y * self.pixel_to_meters, self._size[0], self._size[1]))
