import random
from pygame import Surface
from src.library.object.object import Object
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector
from src.library.pygame.keys import Keys
from src.library.constants.game_config_constants import GameConfigConstants
import pygame


class Enemy(Object):

    def __init__(self, screen: Surface, position: Vector) -> None:
        super().__init__()
        self.game_config_constants = GameConfigConstants()
        self.pygame_engine = PygameEngine()
        self._screen: Surface = screen
        if position is None:
            position = Vector(
                random.randint(0, self._screen.get_width() - 1),
                random.randint(0, self._screen.get_height() - 1)
            )
        self._size_nav = [80, 80]
        self._pixel_to_meters = 20
        self._enemy_speed_default = 30
        self._sprite = self.pygame_engine.load_sprite_image(
            self.game_config_constants.ENEMY_SPACESHIP_SPRITE)
        self._sprite = self.pygame_engine.scale_sprite(
            self._sprite, self._size_nav[0], self._size_nav[1]
        )
        self._move_timer = 0
        self._move_interval = 2.0  # Intervalo aumentado para evitar mudanças frequentes
        self._current_direction = Vector(1, 0)
        self._direction = random.choice(['left', 'right', 'up', 'down'])
        self._speed = Vector(0, 0)

    def move_enemy(self, delta_time: float) -> None:
        self._move_timer += delta_time

        if self._move_timer >= self._move_interval:
            self._move_timer = 0
            self._direction = random.choice(['left', 'right', 'up', 'down'])

        if self._direction == 'left':
            self._speed = Vector(-self._enemy_speed_default, 0)
        elif self._direction == 'right':
            self._speed = Vector(self._enemy_speed_default, 0)
        elif self._direction == 'up':
            self._speed = Vector(0, -self._enemy_speed_default)
        elif self._direction == 'down':
            self._speed = Vector(0, self._enemy_speed_default)

        new_position = Vector(
            self._position.x + self._speed.x * delta_time,
            self._position.y + self._speed.y * delta_time
        )

        # Verificar limites da tela
        if 0 <= new_position.x <= self._screen.get_width() / self._pixel_to_meters - self._size_nav[0] / self._pixel_to_meters and 0 <= new_position.y <= self._screen.get_height() / self._pixel_to_meters - self._size_nav[1] / self._pixel_to_meters:
            self._position = new_position

    def draw_object(self) -> None:
        self._screen.blit(self._sprite, (self._position.x *
                          self._pixel_to_meters, self._position.y * self._pixel_to_meters))
