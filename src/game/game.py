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
# from src.lib.object.object import Object


class Game:
    
    def __init__(self):
        pygame.display.init()
        self.setup = Setup()
        self.running = True
        self.screen = self.setup.screen
        self.spaceship = Spaceship(self.screen, None)
        self.objects = []
        # self.add_objects(self.spaceship)
        
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
            self.spaceship._position.x += (keys[K_RIGHT] - keys[K_LEFT]) * self.spaceship._speed * (dt / 1000)
            self.spaceship._position.y += (keys[K_DOWN] - keys[K_UP]) * \
                self.spaceship._speed * (dt / 1000)
            
            self.screen.fill("black")
            
            pixel_to_meters = 20
            
            pygame.draw.rect(
                self.screen, (255, 0, 0), 
                (self.spaceship._position.x * pixel_to_meters, self.spaceship._position.y *
                 pixel_to_meters, self.spaceship._size * pixel_to_meters, self.spaceship._size * pixel_to_meters)
            )
            
            pygame.display.flip()

            

        pygame.display.quit()
        
    # def add_objects(self, object: Object):
    #     self.objects.append(object)