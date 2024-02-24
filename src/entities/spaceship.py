import pygame
from config.setup import Setup

class Spaceship:
    
    def __init__(self):
        self.setup = Setup()
        self.screen = self.setup.screen
        self.position = pygame.Vector2(
            self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.size = 30
        self.speed = 5
