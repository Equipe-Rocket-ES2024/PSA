from typing import Tuple
from pygame import Surface
import pygame
from abc import ABC, abstractmethod

from src.library.vector.vector import Vector


class Engine(ABC):
    
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def display_init(self):
        pass
    
    @abstractmethod
    def start_clock(self) -> int:
        pass
    
    @abstractmethod
    def display_quit(self) -> None:
        pass
    
    @abstractmethod
    def display_flip(self) -> None:
        pass
    
    @abstractmethod
    def get_key_pressed(self) -> float:
        pass
    
    @abstractmethod
    def default_position(self, pos_x: int, pos_y: int) -> pygame.Vector2:
        pass
    
    @abstractmethod
    def draw_rect(
        self, 
        screen: Surface, 
        color: Tuple[int, int, int], 
        position: Vector, 
        size: Tuple[int, int], 
        pixel_to_meters: int
    ) -> None:
        pass
    
    @abstractmethod
    def load_sprite_image(self, path_image: str) -> Surface:
        pass
    
    @abstractmethod
    def scale_sprite(
        self, 
        sprite: Surface, 
        width: int, 
        height: int
    ) -> Surface:
        pass
