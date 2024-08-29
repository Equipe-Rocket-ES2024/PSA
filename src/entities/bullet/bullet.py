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
        self.screen: Surface = screen
        starting_x = position.x + 1.7
        starting_y = position.y - self.size[1] - 1
        self.position = self.pygame_engine.default_position(starting_x, starting_y)
        self.size = [10, 10]
        self.bullet_speed_default = 30
        self.sprite = self.pygame_engine.load_sprite_image(
            self.game_config_constants.BULLET_SPRITE)
        self.sprite = self.pygame_engine.scale_sprite(
            self.sprite, self.size[0], self.size[1]
        )
        self.color = pygame.Color('white')
        self.hitbox = Hitbox(self, Vector(1, 1), Vector(0, 0))

    def move_object(self) -> None:
        self._speed.y = -self.bullet_speed_default
        
    
    def physics_process(self, delta_time: float, screen_width: int, screen_height: int) -> None:
        super().physics_process(delta_time, screen_width, screen_height)
        self.hitbox.update()
        