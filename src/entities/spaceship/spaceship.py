from pygame import Surface
import pygame
from src.library.object.object import Object
from src.library.vector.vector import Vector


class Spaceship(Object):

    def __init__(self, screen: Surface, position: Vector) -> None:
        self._screen: Surface = screen
        self._position = pygame.Vector2(4, 5)
        self._size = 2
        self._speed = 10
