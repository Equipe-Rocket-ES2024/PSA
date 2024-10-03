from typing import List
from pygame import Surface
from src.library.enums.direction_movimentation_enum import DirectionMovimentationEnum
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector


class SpriteManager:
    def __init__(self, sprites_list: List[Surface], size: Vector) -> Surface:
        self.pygame_engine = PygameEngine()
        self.size = size
        self.sprites = sprites_list
        self.current_sprite = self.sprites[0]
        self.current_sprite = self.pygame_engine.scale_sprite(
            self.current_sprite, self.size[0], self.size[1])

    def update_sprite(self, direction_index: DirectionMovimentationEnum) -> None:
        self.current_sprite = self.sprites[direction_index]
