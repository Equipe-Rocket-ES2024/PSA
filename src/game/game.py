import pygame
from src.entities.enemy.enemy import Enemy
from src.entities.bullet.bullet import Bullet
from src.entities.spaceship.spaceship import Spaceship
from src.config.setup import Setup
from src.library.hitbox.hitbox import Hitbox
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
                    if event.type == pygame.KEYDOWN and event.key == Keys.K_SPACE.value:
                        self.add_objects(Bullet(self.screen, self.spaceship.position))
                        
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
        for obj in self.objects:
            obj.physics_process(delta_time, self.screen.get_width(), self.screen.get_height())
            
            if isinstance(obj, Enemy):
                obj.move_object(self.delta_time)
            elif isinstance(obj, Bullet):
                obj.move_object()

        for i in range(len(self.objects)):
            for j in range(i + 1, len(self.objects)):
                obj1 = self.objects[i]
                obj2 = self.objects[j]
                if Hitbox.check_collision(obj1.hitbox, obj2.hitbox):
                    print(f"Collision detected between {type(obj1).__name__} and {type(obj2).__name__}")
                            
                
    def render(self):
        self.screen.fill(self.game_config_constants.GAME_BACKGROUND_COLOR)

        for object in self.objects:
            object.draw_object()

        self.pygame_engine.display_flip()
        
