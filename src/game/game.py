import pygame
from src.entities.enemy.enemy import Enemy
from src.entities.bullet.bullet import Bullet
from src.entities.spaceship.spaceship import Spaceship
from src.config.setup import Setup
from src.library.background.background import Background
from src.library.constants.enemy_constants import EnemyConstants
from src.library.hitbox.hitbox import Hitbox
from src.library.pygame.pygame import PygameEngine
from src.library.object.object import Object
from src.library.pygame.keys import Keys
from src.library.constants.game_config_constants import GameConfigConstants
from src.library.constants.spaceship_constants import SpaceshipConstants
from src.library.constants.scenario_constants import ScenarioConstants
import itertools

from src.library.vector.vector import Vector

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
        self.enemies_pending_removal = []
        self.background_game_list = [
            Background(
                ScenarioConstants.BACKGROUND_01, 
                Vector(0, 3),
                self.screen,
            ),
        ]
        
        
    def run_game(self):
        while self.running:            
            for event in self.pygame_engine.get_events():
                if event.type == Keys.QUIT.value:
                    self.running = False
                    self.pygame_engine.display_quit()
                    break
                
                elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                    self.spaceship.change_speed(event)
                    if event.type == pygame.KEYDOWN and event.key == Keys.K_SPACE.value:
                        self.add_objects(self.spaceship.shoot())
                        
                elif event.type == Keys.KEYDOWN.value:
                    if event.key == Keys.K_ESCAPE.value:
                        self.running = False
                        self.pygame_engine.display_quit()

                             
            self.delta_time = (self.clock.tick(60) / 1000)
            
            self.physics_process(self.delta_time)
            self.update_enemy_removals()
            self.remove_out_of_bounds_bullets()
            
            self.render()
        
        self.display_game_over()
        self.pygame_engine.display_init()
        

    def add_objects(self, object: Object) -> None:
        self.objects.append(object)
        
        
    def physics_process(self, delta_time: float) -> None:
        for obj in self.objects:
            obj.physics_process(
                delta_time, 
                self.screen.get_width(), 
                self.screen.get_height()
            )

            if isinstance(obj, Enemy):
                obj.change_speed(self.delta_time)
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
        self.paralax()

        for object in self.objects:
            object.draw_object(self.screen)

        score_text = self.font.render(
            f"{self.game_config_constants.SCORE_LABEL}: {self.score}", 
            True, 
            (255, 255, 255)
        )
        self.screen.blit(score_text, (10, 10))
        
        self.draw_hearts()
        
        self.pygame_engine.display_flip()
        

    def draw_hearts(self) -> None:
        heart_spacing = 40
        position_x = 10
        position_y = 50
        for i in range(self.lives):
            x_position = position_x + i * heart_spacing
            self.screen.blit(
                self.heart_sprite, 
                (x_position, position_y)
            )


    def handle_collision(self):
        objects_remove = set()

        for obj1, obj2 in itertools.combinations(self.objects, 2):
            if Hitbox.check_collision(obj1.hitbox, obj2.hitbox):
                self.handle_enemy_bullet_collision(obj1, obj2, objects_remove)
                self.handle_enemy_spaceship_collision(obj1, obj2, objects_remove)

        self.remove_objects(objects_remove)


    def handle_enemy_bullet_collision(self, obj1, obj2, objects_remove):
        if isinstance(obj1, Enemy) and isinstance(obj2, Bullet):
            self.schedule_enemy_removal(obj1)
            obj1.explosion(EnemyConstants.ENEMY_EXPLOSION)
            obj1.stop_movement()
            self.score += 1
            objects_remove.add(obj2)
        elif isinstance(obj1, Bullet) and isinstance(obj2, Enemy):
            self.schedule_enemy_removal(obj1)
            obj2.explosion(EnemyConstants.ENEMY_EXPLOSION)   
            obj2.stop_movement()
            objects_remove.add(obj1)         
            self.score += 1
    
    
    def handle_enemy_spaceship_collision(self, obj1, obj2, objects_remove):
        if isinstance(obj1, Spaceship) and isinstance(obj2, Enemy):
            obj1.explosion(SpaceshipConstants.SPACESHIP_EXPLOSION)
            self.lives -= 1
            objects_remove.add(obj2)
            if self.lives <= 0:
                self.running = False
        elif isinstance(obj1, Enemy) and isinstance(obj2, Spaceship):
            obj2.explosion(SpaceshipConstants.SPACESHIP_EXPLOSION)
            self.lives -= 1
            objects_remove.add(obj1)
            if self.lives <= 0:
                self.running = False
            

    def remove_objects(self, objects_remove):
        self.objects = [obj for obj in self.objects if obj not in objects_remove]


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
        
    
    def schedule_enemy_removal(self, enemy):
        removal_time = self.pygame_engine.get_ticks() + 100
        self.enemies_pending_removal.append((enemy, removal_time))


    def update_enemy_removals(self):
        current_time = self.pygame_engine.get_ticks()
        enemies_to_remove = [
            enemy for enemy, removal_time in self.enemies_pending_removal if current_time >= removal_time
        ]
  
        self.objects = [obj for obj in self.objects if obj not in enemies_to_remove]
        self.enemies_pending_removal = [
            (enemy, removal_time) for enemy, removal_time in self.enemies_pending_removal
            if enemy not in enemies_to_remove
        ]
        
    
    def paralax(self):
        for background in self.background_game_list:
            background.paralax()
            background.draw()


    def menu_inicial(self):
        font_button = pygame.font.Font(None, 60)
        font_title = pygame.font.Font(None, 100)
        
        start_text = font_button.render("Start", True, (255, 255, 255))
        exit_text = font_button.render("Exit", True, (255, 255, 255))
        
        start_button_rect = pygame.Rect((self.screen.get_width() // 2 - 100, 300, 200, 80))
        exit_button_rect = pygame.Rect((self.screen.get_width() // 2 - 100, 450, 200, 80))
        
        game_title_text = font_title.render("Star Wars X Star Treek", True, (255, 255, 0))
        title_rect = game_title_text.get_rect(center=(self.screen.get_width() // 2, 100))
        
        menu_running = True
        while menu_running:
            self.screen.fill((0, 0, 0))

            self.screen.blit(game_title_text, title_rect)

            pygame.draw.rect(self.screen, (0, 0, 255), start_button_rect)
            pygame.draw.rect(self.screen, (255, 0, 0), exit_button_rect)

            self.screen.blit(start_text, (start_button_rect.x + 50, start_button_rect.y + 20))
            self.screen.blit(exit_text, (exit_button_rect.x + 65, exit_button_rect.y + 20))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(event.pos):
                        return True
                    elif exit_button_rect.collidepoint(event.pos):
                        return False

            pygame.display.flip()
                    
    
    def reset_game(self):
        self.lives = 3
        self.score = 0 
        self.objects = [self.spaceship]
        self.enemies_pending_removal = []
        self.running = True


    def display_game_over(self):
        font = pygame.font.Font(None, 74)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        restart_text = font.render("Returning to Menu...", True, (255, 255, 255))

        self.screen.fill((0, 0, 0))  # Limpa a tela
        self.screen.blit(game_over_text, (self.screen.get_width() // 2 - game_over_text.get_width() // 2, 200))
        self.screen.blit(restart_text, (self.screen.get_width() // 2 - restart_text.get_width() // 2, 300))

        pygame.display.flip()
        pygame.time.wait(2000)  # Espera 2 segundos antes de voltar ao menu
        self.reset_game()
        if self.menu_inicial():
            self.run_game()
