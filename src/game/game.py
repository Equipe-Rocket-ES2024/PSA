import pygame
from src.entities.spaceship.spaceship import Spaceship
from src.config.setup import Setup
from src.library.pygame.pygame import PygameEngine
from src.library.object.object import Object
from src.library.pygame.keys import Keys


class Game:
    
    def __init__(self):
        self.pygame_engine = PygameEngine()
        self.pygame_engine.display_init()
        self.setup = Setup()
        self.running = True
        self.screen = self.setup.screen
        self.spaceship = Spaceship(self.screen, None)
        self.objects = []
        self.add_objects(self.spaceship)
        
    def run_game(self):
        clock = self.pygame_engine.start_clock()
        
        while self.running:
            
            for event in pygame.event.get():
                if event.type == Keys.QUIT.value:
                    self.running = False
                    self.pygame_engine.display_quit()
                    break
                
                elif event.type == Keys.KEYDOWN.value:
                    if event.key == Keys.K_ESCAPE.value:
                        self.running = False
                        self.pygame_engine.display_quit()
                        


            if self.running == False:
                break
            
            keys = pygame.key.get_pressed()
            
            dt = clock.tick(60)          
            
            self.spaceship._position.x += (
                keys[Keys.K_RIGHT.value] - keys[Keys.K_LEFT.value]) * self.spaceship._speed * (dt / 1000)
            self.spaceship._position.y += (
                keys[Keys.K_DOWN.value] - keys[Keys.K_UP.value]) * self.spaceship._speed * (dt / 1000)
            
            self.screen.fill("black")
            
            pixel_to_meters = 20
            
            pygame.draw.rect(
                self.screen, (255, 0, 0), 
                (self.spaceship._position.x * pixel_to_meters, self.spaceship._position.y *
                 pixel_to_meters, self.spaceship._size * pixel_to_meters, self.spaceship._size * pixel_to_meters)
            )
            
            pygame.display.flip()

        pygame.display.quit()
        
    def add_objects(self, object: Object):
        self.objects.append(object)
        
