import pygame
from config.setup import Setup
from entities.spaceship import Spaceship
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    QUIT,
    K_ESCAPE,
    KEYDOWN
)

class Game:
    
    def __init__(self):
        pygame.init()
        self.setup = Setup()
        self.running = True
        self.screen = self.setup.screen
        self.spaceship = Spaceship(self.screen)
        
    def run_game(self):
        clock = pygame.time.Clock()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

            keys = pygame.key.get_pressed()

            self.spaceship.position.x += (keys[K_RIGHT] - keys[K_LEFT]) * self.spaceship.speed
            
            self.spaceship.position.y += (keys[K_DOWN] - keys[K_UP]) * self.spaceship.speed
            
            self.screen.fill("black")
            
            pygame.draw.rect(
                self.screen, (255, 0, 0), 
                (self.spaceship.position.x,self.spaceship.position.y, self.spaceship.size, self.spaceship.size)
            )

            pygame.display.flip()

            clock.tick(60)

        pygame.display.quit()