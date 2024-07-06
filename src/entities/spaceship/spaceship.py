from pygame import Surface
from src.library.object.object import Object
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector
from src.library.pygame.keys import Keys
import pygame


class Spaceship(Object):

    def __init__(self, screen: Surface, position: Vector) -> None:
        super().__init__()
        self.pygame_engine = PygameEngine()
        self._screen: Surface = screen
        self._position = self.pygame_engine.default_position(18, 35)
        self._size = 2
        self.pixel_to_meters = 20
        self.spaceship_speed_default = 10
        
    def move_spaceship(self, event: pygame.event.EventType) -> None:
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

    def draw_spaceship(self) -> None:
        self.pygame_engine.draw_rect(
            self._screen, (255, 0, 0), self._position, self._size, self.pixel_to_meters)
