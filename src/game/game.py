import pygame
from config.setup import Setup
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    QUIT
)

class Game:
    
    def __init__(self):
        pygame.init()
        self.setup = Setup()
        self.screen = pygame.display.set_mode(
            (self.setup.screen_width, self.setup.screen_height))
        pygame.display.set_caption(self.setup.game_name)
        self.running = True
        
    def run_game(self):
        clock = pygame.time.Clock()
        player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        player_size = 30  
        player_speed = 5 

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()

            player_pos.x += (keys[K_RIGHT] - keys[K_LEFT]) * player_speed
            player_pos.y += (keys[K_DOWN] - keys[K_UP]) * player_speed
            
            self.screen.fill("black")
            pygame.draw.rect(self.screen, (255, 0, 0), (player_pos.x,
                            player_pos.y, player_size, player_size))

            pygame.display.flip()

            clock.tick(60)

        pygame.display.quit()

        
    
        
        
    
# pygame setup

