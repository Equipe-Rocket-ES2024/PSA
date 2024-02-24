import pygame

class Spaceship:
    
    def __init__(self, screen):
        self.screen = screen
        self.position = pygame.Vector2(
            self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.size = 30
        self.speed = 5
