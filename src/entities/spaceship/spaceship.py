from pygame import Surface
from src.library.hitbox.hitbox import Hitbox
from src.library.object.object import Object
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector
from src.entities.bullet.bullet import Bullet
from src.library.pygame.keys import Keys
from src.library.constants.game_config_constants import GameConfigConstants

import pygame


class Spaceship(Object):

    def __init__(self, screen: Surface) -> None:
        super().__init__()
        self.game_config_constants = GameConfigConstants()
        self.pygame_engine = PygameEngine()
        self.screen: Surface = screen
        self.position = self.pygame_engine.default_position(18, 35)
        self.size = [50, 50]
        self.spaceship_speed_default = 20
        self.sprite = self.pygame_engine.load_sprite_image(self.game_config_constants.PLAYER_SPACESHIP_SPRITE)
        self.sprite = self.pygame_engine.scale_sprite(
            self.sprite, self.size[0], self.size[1])
        self.hitbox = Hitbox(self, Vector(1, 1), Vector(0, 0))

        
    def move_object(self, event: pygame.event.EventType) -> None:        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self._speed.x = self.spaceship_speed_default
            elif event.key == pygame.K_LEFT:
                self._speed.x = -self.spaceship_speed_default
            elif event.key == pygame.K_DOWN:
                self._speed.y = self.spaceship_speed_default
            elif event.key == pygame.K_UP:
                self._speed.y = -self.spaceship_speed_default
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                self._speed.x = 0
            elif event.key in [pygame.K_DOWN, pygame.K_UP]:
                self._speed.y = 0
                
                
    def physics_process(self, delta_time: float, screen_width: int, screen_height: int) -> None:
        super().physics_process(delta_time, screen_width, screen_height)
        self.hitbox.update()
        
        
    def shoot(self) -> Bullet:
        return Bullet(self.screen, self.position)

    
