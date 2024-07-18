import pygame
from src.entities.enemy.enemy import Enemy
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
        self.objects = [self.spaceship]
        self.clock = self.pygame_engine.start_clock()
        self.delta_time = 0
        self.game_config_constants = GameConfigConstants()
        self.enemy = Enemy(self.screen, None)
        self.add_objects(self.enemy)
        
    def run_game(self):
        
        while self.running:
            
            for event in pygame.event.get():
                if event.type == Keys.QUIT.value:
                    self.running = False
                    self.pygame_engine.display_quit()
                    break
                
                elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                    self.spaceship.move_object(event)
                
                elif event.type == Keys.KEYDOWN.value:
                    if event.key == Keys.K_ESCAPE.value:
                        self.running = False
                        self.pygame_engine.display_quit()

            if self.running == False:
                break
                             
            self.delta_time = (self.clock.tick(60) / 1000)
            
            self.physics_process(self.delta_time)
            
            self.render()

        self.pygame_engine.display_init()
        
    def add_objects(self, object: Object) -> None:
        self.objects.append(object)
        
    def physics_process(self, delta_time: float) -> None:
        limit_screen_width = self.setup.screen_width / 22
        limit_screen_height = self.setup.screen_height / 22
        
        for object in self.objects:
            object.physics_process(
                delta_time, limit_screen_width, limit_screen_height
            )
            
            if isinstance(object, Enemy):
                object.move_enemy(self.delta_time)
                
    def render(self):
        self.screen.fill(self.game_config_constants.GAME_BACKGROUND_COLOR)

        for object in self.objects:
            object.draw_object()

        self.pygame_engine.display_flip()
        
