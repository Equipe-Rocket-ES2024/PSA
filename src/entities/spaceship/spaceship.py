from pygame import Surface
from src.library.object.object import Object
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector
from src.library.pygame.keys import Keys


class Spaceship(Object):
    
    def __init__(self, screen: Surface, position: Vector) -> None:
        self.pygame_engine = PygameEngine()
        self._screen: Surface = screen
        self._position = self.pygame_engine.default_position(18, 35)
        self._size = 2
        self._speed = 10
        self.pixel_to_meters = 20
        self._sprite = ""
        
    def move_spaceship(self, delta_time: int) -> None:
        keys = self.pygame_engine.get_key_pressed()
        self._position.x += (
            keys[Keys.K_RIGHT.value] - keys[Keys.K_LEFT.value]) * self._speed * (delta_time / 1000)
        self._position.y += (
            keys[Keys.K_DOWN.value] - keys[Keys.K_UP.value]) * self._speed * (delta_time / 1000)
        
    def draw_spaceship(self) -> None:
        self.pygame_engine.draw_rect(self._screen, (255, 0, 0), self._position, self._size, self.pixel_to_meters)
