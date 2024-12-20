from pygame import Surface
from src.library.hitbox.hitbox import Hitbox
from src.library.object.object import Object
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector
from src.library.constants.bullet_constants import BulletConstants
import pygame
from copy import copy


class Bullet(Object):

    def __init__(self, screen: Surface, position: Vector, speed_bullet: Vector) -> None:
        super().__init__()
        self.pygame_engine = PygameEngine()
        self.screen: Surface = screen
        starting_x = position.x
        starting_y = position.y - self.size[1]
        self.position = self.pygame_engine.default_position(starting_x, starting_y)
        self.size = [10, 10]
        self.sprite = self.pygame_engine.load_sprite_image(
            BulletConstants.BULLET_SPRITE
        )
        self.sprite = self.pygame_engine.scale_sprite(
            self.sprite, self.size[0], self.size[1]
        )
        self._speed = copy(speed_bullet)
        self.color = self.pygame_engine.color('white')
        self.hitbox = Hitbox(self, Vector(1, 1), Vector(0, 0))
        
    
    def physics_process(self, delta_time: float, screen_width: int, screen_height: int) -> None:
        super().physics_process(delta_time, screen_width, screen_height)
        self.hitbox.update()