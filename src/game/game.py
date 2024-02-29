import pygame
from src.entities.spaceship.spaceship import Spaceship
from src.config.setup import Setup
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
        pygame.display.init()
        self.setup = Setup()
        self.running = True
        self.screen = self.setup.screen
        self.spaceship = Spaceship(self.screen, None)
        
    def run_game(self):
        clock = pygame.time.Clock()
        
        while self.running:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.quit()
                    break
                
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                        pygame.quit()

            if self.running == False:
                break
            
            keys = pygame.key.get_pressed()
            
            dt = clock.tick(60)          
            
            # ALTERAR O CALCULO DE VELOCIDADE
            self.spaceship._position.x += (keys[K_RIGHT] - keys[K_LEFT]) * self.spaceship._speed * dt
            self.spaceship._position.y += (keys[K_DOWN] - keys[K_UP]) * \
                self.spaceship._speed * dt
            
            self.screen.fill("black")
            
            pygame.draw.rect(
                self.screen, (255, 0, 0), 
                (self.spaceship._position.x,self.spaceship._position.y, self.spaceship._size, self.spaceship._size)
            )
            
            pygame.display.flip()

            

        pygame.display.quit()