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
from src.library.constants.spaceship_constants import SpaceshipConstants
from src.library.constants.scenario_constants import ScenarioConstants

class Game:
    
    def __init__(self):
        self.pygame_engine = PygameEngine()
        self.pygame_engine.display_init()
        self.setup = Setup()
        self.running = True
        self.screen = self.setup.screen
        self.spaceship = Spaceship(self.screen)
        self.objects = [self.spaceship]
        self.clock = self.pygame_engine.start_clock()
        self.delta_time = 0
        self.game_config_constants = GameConfigConstants()
        self.enemy = Enemy(self.screen)
        self.add_objects(self.enemy)
        self.enemy_spawn_interval = 2
        self.time_since_last_spawn = 0
        self.score = 0
        self.pygame_engine.font_init()
        self.font = pygame.font.Font(None, 36)
        self.lives = 3
        self.heart_sprite = self.pygame_engine.load_sprite_image(ScenarioConstants.HEART_01)
        self.heart_sprite = self.pygame_engine.scale_sprite(self.heart_sprite, 40, 30)
        
        
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
                        spaceshipAliveList = list(
                            filter(self.spaceshipAlive, self.objects))
                        if (spaceshipAliveList.__len__() > 0):
                            self.add_objects(self.spaceship.shoot())
                        
                elif event.type == Keys.KEYDOWN.value:
                    if event.key == Keys.K_ESCAPE.value:
                        self.running = False
                        self.pygame_engine.display_quit()

            if self.running == False:
                break
                             
            self.delta_time = (self.clock.tick(60) / 1000)
            
            self.physics_process(self.delta_time)

            self.remove_out_of_bounds_bullets()
            
            self.render()

        self.pygame_engine.display_init()
        

    def add_objects(self, object: Object) -> None:
        self.objects.append(object)
        
        
    def physics_process(self, delta_time: float) -> None:
        for obj in self.objects:
            obj.physics_process(
                delta_time, self.screen.get_width(), self.screen.get_height())

            if isinstance(obj, Enemy):
                obj.move_object(self.delta_time)
                bullet = obj.update(delta_time)
                if bullet:
                    self.add_objects(bullet)

            self.handle_collision()

        self.time_since_last_spawn += delta_time
        if self.time_since_last_spawn >= self.enemy_spawn_interval:
            self.spawn_enemy()
            self.time_since_last_spawn = 0


    def render(self):
        self.screen.fill(self.game_config_constants.GAME_BACKGROUND_COLOR)

        for object in self.objects:
            object.draw_object(self.screen)

        score_text = self.font.render(f"{self.game_config_constants.SCORE_LABEL}: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        
        for i in range(self.lives):
            self.screen.blit(self.heart_sprite, (10 + i * 40, 50))

        self.pygame_engine.display_flip()


    def handle_collision(self): 
        objects_remove = [];
        for i in range(len(self.objects)):
            for j in range(i + 1, len(self.objects)):
                if self.objects and len(self.objects) > 0:
                    obj1 = self.objects[i]
                    obj2 = self.objects[j]
                if Hitbox.check_collision(obj1.hitbox, obj2.hitbox):
                    if (isinstance(obj1, Enemy) and isinstance(obj2, Bullet)) or (isinstance(obj1, Bullet) and isinstance(obj2, Enemy)):
                        objects_remove.append(obj1)
                        objects_remove.append(obj2)
                        self.score += 1
                    if (isinstance(obj1, Spaceship) and isinstance(obj2, Bullet)) or (isinstance(obj1, Bullet) and isinstance(obj2, Spaceship)):
                        if isinstance(obj1, Spaceship):
                            obj1.explosion(SpaceshipConstants.SPACESHIP_EXPLOSION)
                        elif isinstance(obj2, Spaceship):
                            obj2.explosion(SpaceshipConstants.SPACESHIP_EXPLOSION)
                        self.lives -= 1
                        objects_remove.append(obj2)
                        if self.lives <= 0:
                            self.running = False
                    
        
        self.objects = list(
            filter(lambda x: x not in objects_remove, self.objects))


    def remove_out_of_bounds_bullets(self):
        objects_to_remove = []
        
        for obj in self.objects:
            if isinstance(obj, Bullet):
                max_x = (self.setup.screen_width / obj.meters_to_pixel) - (obj.size[0] / obj.meters_to_pixel)
                max_y = (self.setup.screen_height / obj.meters_to_pixel) - (obj.size[1] / obj.meters_to_pixel)
                if obj.position.y <= 0 or obj.position.x <= 0 or obj.position.y >= max_x or obj.position.x >= max_y:
                    objects_to_remove.append(obj)
        
        self.objects = list(filter(lambda x: x not in objects_to_remove, self.objects))


    def spawn_enemy(self):
        new_enemy = Enemy(self.screen)
        self.add_objects(new_enemy)

        
    def spaceshipAlive(self, obj):
        return isinstance(obj, Spaceship)