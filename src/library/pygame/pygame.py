from typing import Tuple
from src.library.engine.engine import Engine
import pygame
from pygame import Surface
from src.library.vector.vector import Vector
from src.library.constants.game_config_constants import GameConfigConstants

class PygameEngine(Engine):
    
    def __init__(self) -> None:
        self.game_config_constants = GameConfigConstants()
        pass
    
    def display_init(self) -> None:
        return pygame.display.init()
    
    def start_clock(self) -> int:
        return pygame.time.Clock()
    
    def display_quit(self) -> None:
        return pygame.quit()

    def display_flip(self) -> None:
        return pygame.display.flip()
    
    def get_key_pressed(self) -> int:
        return pygame.key.get_pressed()
    
    def default_position(self, pos_x: int, pos_y: int) -> pygame.Vector2:
        return pygame.Vector2(pos_x, pos_y)
    
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
        
    def load_sprite_image(self, src_sprite: str) -> Surface:
        return pygame.image.load(self.game_config_constants.GAME_BACKGROUND_COLOR).convert_alpha()
