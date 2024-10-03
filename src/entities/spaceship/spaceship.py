from pygame import Surface
from src.library.hitbox.hitbox import Hitbox
from src.library.sprite_manager.sprite_manager import SpriteManager
from src.library.object.object import Object
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector
from src.entities.bullet.bullet import Bullet
from src.library.constants.game_config_constants import GameConfigConstants
from src.library.constants.spaceship_constants import SpaceshipConstants
from src.library.enums.direction_movimentation_enum import DirectionMovimentationEnum

import pygame


class Spaceship(Object):

    def __init__(self, screen: Surface) -> None:
        super().__init__()
        self.game_config_constants = GameConfigConstants()
        self.pygame_engine = PygameEngine()
        self.screen: Surface = screen
        self.position = self.pygame_engine.default_position(18, 35)
        self.size = [50, 50]
        self.spaceship_scalar_speed = 20
        # self.sprites = [
        #     self.pygame_engine.load_sprite_image(self.game_config_constants.PLAYER_SPACESHIP_SPRITE_RIGHT),
        #     self.pygame_engine.load_sprite_image(self.game_config_constants.PLAYER_SPACESHIP_SPRITE_LEFT),
        #     self.pygame_engine.load_sprite_image(self.game_config_constants.PLAYER_SPACESHIP_SPRITE_DOWN),
        #     self.pygame_engine.load_sprite_image(self.game_config_constants.PLAYER_SPACESHIP_SPRITE_UP),
        #     self.pygame_engine.load_sprite_image(self.game_config_constants.EXPLOSION),
        # ]
        self.sprites = [
            self.pygame_engine.load_sprite_image(value)
            for key, value in vars(SpaceshipConstants).items()
            if not key.startswith("__")
        ]
        self.sprite_manager = SpriteManager(self.sprites, self.size)
        self.sprite = self.sprite_manager.current_sprite
        self.sprite = self.pygame_engine.scale_sprite(self.sprite, self.size[0], self.size[1])
        self.direction_movimentation = DirectionMovimentationEnum.UP_SIDE.value
        self.hitbox = Hitbox(self, Vector(1, 1), Vector(0, 0))

        
    def move_object(self, event: pygame.event.EventType) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.direction_movimentation = DirectionMovimentationEnum.RIGHT_SIDE.value
                self._speed.x = self.spaceship_scalar_speed
            elif event.key == pygame.K_LEFT:
                self.direction_movimentation = DirectionMovimentationEnum.LEFT_SIDE.value
                self._speed.x = -self.spaceship_scalar_speed
            elif event.key == pygame.K_DOWN:
                self.direction_movimentation = DirectionMovimentationEnum.DOWN_SIDE.value
                self._speed.y = self.spaceship_scalar_speed
            elif event.key == pygame.K_UP:
                self.direction_movimentation = DirectionMovimentationEnum.UP_SIDE.value
                self._speed.y = -self.spaceship_scalar_speed
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                self._speed.x = 0
            elif event.key in [pygame.K_DOWN, pygame.K_UP]:
                self._speed.y = 0
                
        self.sprite_manager.update_sprite(self.direction_movimentation)
        self.sprite = self.sprite_manager.current_sprite
                
                
    def physics_process(self, delta_time: float, screen_width: int, screen_height: int) -> None:
        super().physics_process(delta_time, screen_width, screen_height)
        self.hitbox.update()
        
        
    def shoot(self) -> Bullet:
        position_shoot = Vector(self.position.x, self.position.y)
        speed_shoot = Vector(0, 0)
        scalar_speed = 30
        delta = 1

        if self.direction_movimentation == DirectionMovimentationEnum.RIGHT_SIDE.value:  
            position_shoot.x += delta
            speed_shoot.x = scalar_speed
            speed_shoot.y = 0
        elif self.direction_movimentation == DirectionMovimentationEnum.LEFT_SIDE.value:
            position_shoot.x -= delta  
            speed_shoot.x = -scalar_speed
            speed_shoot.y = 0
        elif self.direction_movimentation == DirectionMovimentationEnum.DOWN_SIDE.value:  
            position_shoot.y += delta 
            speed_shoot.x = 0
            speed_shoot.y = scalar_speed 
        elif self.direction_movimentation == DirectionMovimentationEnum.UP_SIDE.value:
            position_shoot.y -= delta 
            speed_shoot.x = 0
            speed_shoot.y = -scalar_speed  

        return Bullet(self.screen, position_shoot, speed_shoot)



    def explosion(self, sprite):
        self.sprite = self.pygame_engine.load_sprite_image(sprite)
        self.sprite = self.pygame_engine.scale_sprite(
            self.sprite, self.size[0], self.size[1])