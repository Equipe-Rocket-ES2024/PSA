import pygame
from src.entities.spaceship.spaceship import Spaceship
from src.config.setup import Setup
from src.library.pygame.pygame import PygameEngine
from src.library.object.object import Object
from src.library.pygame.keys import Keys
from src.library.constants.game_config_constants import GameConfigConstants

class Game:
    
    def __init__(self):
        self.pygame_engine = PygameEngine()
        self.pygame_engine.display_init()
        self.setup = Setup()
        self.running = True
        self.screen = self.setup.screen
        self.spaceship = Spaceship(self.screen, None)
        self.objects = []
        self.clock = self.pygame_engine.start_clock()
        self.delta_time = 0
        self.game_config_constants = GameConfigConstants()
        self.add_objects(self.spaceship)
        
    def run_game(self):
        
        while self.running:
            
            for event in pygame.event.get():
                if event.type == Keys.QUIT.value:
                    self.running = False
                    self.pygame_engine.display_quit()
                    break
                
                elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                    self.spaceship.move_spaceship(event)
                
                elif event.type == Keys.KEYDOWN.value:
                    if event.key == Keys.K_ESCAPE.value:
                        self.running = False
                        self.pygame_engine.display_quit()

            if self.running == False:
                break
                             
            self.delta_time = (self.clock.tick(60) / 1000)
            
            self.physics_proccess(self.delta_time)
            
            self.screen.fill(self.game_config_constants.GAME_BACKGROUND_COLOR)
            
            self.spaceship.draw_spaceship()
            
            self.pygame_engine.display_flip()

        self.pygame_engine.display_init()
        
    def add_objects(self, object: Object) -> None:
        self.objects.append(object)
        
    def physics_proccess(self, delta_time: float) -> None:
        screen_width = self.setup.screen_width
        screen_height = self.setup.screen_height

        print(screen_width)
        
        for object in self.objects:
            object.physics_proccess(delta_time, screen_width, screen_height)
        