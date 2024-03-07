from pygame import Surface
import pygame
from src.lib.vector.vector import Vector


class Spaceship():

    def __init__(self, screen: Surface, position: Vector):
        self._screen: Surface = screen
        # self._position = pygame.Vector2(
        #     self._screen.get_width() / 2, self._screen.get_height() / 2)
        self._position = pygame.Vector2(4, 5)
        self._size = 2
        self._speed = 10
