from typing import Tuple
from src.library.engine.engine import Engine
import pygame
from pygame import Surface
from src.library.vector.vector import Vector

class PygameEngine(Engine):
    
    def __init__(self) -> None:
        super().__init__()
        pass
    
    def display_init(self) -> None:
        return pygame.display.init()
    
    def start_clock(self) -> float:
        return pygame.time.Clock()
    
    def display_quit(self) -> None:
        return pygame.quit()

    def display_flip(self) -> None:
        return pygame.display.flip()
    
    def get_key_pressed(self) -> int:
        return pygame.key.get_pressed()
    
    def default_position(self, pos_x: float, pos_y: float) -> Vector:
        return Vector(pos_x, pos_y)
    
    def draw_rect(
        self, 
        screen: Surface, 
        color: Tuple[int, int, int], 
        position: Vector, 
        size: Tuple[int, int], 
        pixel_to_meters: int
    ) -> None:
        return pygame.draw.rect(
            screen, (color),
            (position.x * pixel_to_meters, position.y * pixel_to_meters, size * pixel_to_meters, size * pixel_to_meters)
        )    

    def load_sprite_image(self, path_image: str) -> Surface:
        return pygame.image.load(path_image).convert_alpha()

    def scale_sprite(self, sprite: Surface, width: int, height: int) -> Surface:
        return pygame.transform.scale(sprite, (width, height))    
