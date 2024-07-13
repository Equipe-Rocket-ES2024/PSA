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
        self.size_nave = [80, 80]
        self.pixel_to_meters = 20
        self.spaceship_speed_default = 30
        self.sprite = self.pygame_engine.load_sprite_image()
        self.sprite = self.pygame_engine.scale_sprite(self.sprite, self.size_nave[0], self.size_nave[1])
        
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

    def draw_object(self) -> None:
        self._screen.blit(self.sprite, (self._position.x * self.pixel_to_meters, self._position.y * self.pixel_to_meters))
