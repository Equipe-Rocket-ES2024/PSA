import random
from pygame import Surface
from src.library.object.object import Object
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector
from src.library.constants.game_config_constants import GameConfigConstants


class Enemy(Object):

    def __init__(self, screen: Surface, position: Vector) -> None:
        super().__init__()
        self.game_config_constants = GameConfigConstants()
        self.pygame_engine = PygameEngine()
        self._screen: Surface = screen
        if position is None:
            position = Vector(
                random.randint(0, self._screen.get_width() // 2 - 1),
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
        self._move_interval = 0.6
        self._zigzag_step = 0
        self._zigzag_pattern = [
            ('right', 1), ('down', 1), ('left', 1), ('up', 1)]
        self._current_direction = Vector(1, 0)
        self._direction = 'right'
        self._speed = Vector(0, 0)

    def move_object(self, delta_time: float) -> None:
        self._move_timer += delta_time
        
        if self._move_timer >= self._move_interval:
            self._move_timer %= self._move_interval
            self._zigzag_step = (self._zigzag_step + 1) % len(self._zigzag_pattern)
            self._direction = self._zigzag_pattern[self._zigzag_step][0]

        if self._direction == 'left':
            self._speed.x = -self._enemy_speed_default
        elif self._direction == 'right':
            self._speed.x = self._enemy_speed_default
        else:
            self._speed.x = 0

        if self._direction == 'up':
            self._speed.y = -self._enemy_speed_default
        elif self._direction == 'down':
            self._speed.y = self._enemy_speed_default
        else:
            self._speed.y = 0


    def draw_object(self) -> None:
        self._screen.blit(self._sprite, (self._position.x *
                          self._pixel_to_meters, self._position.y * self._pixel_to_meters))
