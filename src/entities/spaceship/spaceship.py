from pygame import Surface
from src.library.object.object import Object
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector
from src.library.pygame.keys import Keys


class Spaceship(Object):

    def __init__(self, screen: Surface, position: Vector) -> None:
        super().__init__()
        self.pygame_engine = PygameEngine()
        self._screen: Surface = screen
        self._position = self.pygame_engine.default_position(18, 35)
        self._size = 2
        self.pixel_to_meters = 20
        self.spaceship_speed_default = 10

    def move_spaceship(self) -> None:
        keys = self.pygame_engine.get_key_pressed()
        if keys[Keys.K_RIGHT.value]:
            self._speed.x = self.spaceship_speed_default
        elif keys[Keys.K_LEFT.value]:
            self._speed.x = -self.spaceship_speed_default

        if keys[Keys.K_DOWN.value]:
            self._speed.y = self.spaceship_speed_default
        elif keys[Keys.K_UP.value]:
            self._speed.y = -self.spaceship_speed_default

    def draw_spaceship(self) -> None:
        self.pygame_engine.draw_rect(
            self._screen, (255, 0, 0), self._position, self._size, self.pixel_to_meters)
