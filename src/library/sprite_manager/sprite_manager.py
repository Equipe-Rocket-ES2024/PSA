import pygame
from pygame.surface import Surface
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector
from src.library.hitbox.hitbox import Hitbox
from src.library.constants.game_config_constants import GameConfigConstants


class SpriteManager:
    def __init__(self, sprites_list, size):
        self.pygame_engine = PygameEngine()
        self.size = size
        self.sprites = sprites_list
        self.current_sprite = self.sprites[0]
        self.current_sprite = self.pygame_engine.scale_sprite(
            self.current_sprite, self.size[0], self.size[1])

    def update_sprite(self, direction_index):
        self.current_sprite = self.sprites[direction_index]
