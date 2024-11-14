from random import randint, uniform
from pygame import Surface
from src.library.hitbox.hitbox import Hitbox
from src.library.sprite_manager.sprite_manager import SpriteManager
from src.library.object.object import Object
from src.library.pygame.pygame import PygameEngine
from src.library.vector.vector import Vector
from src.entities.bullet.bullet import Bullet
from src.library.constants.game_config_constants import GameConfigConstants
from src.library.constants.enemy_constants import EnemyConstants
from src.library.enums.direction_movimentation_enum import DirectionMovimentationEnum


class Enemy(Object):

    def __init__(self, screen: Surface) -> None:
        super().__init__()
        self.game_config_constants = GameConfigConstants()
        self.pygame_engine = PygameEngine()
        self.screen: Surface = screen
        self.position = self._generate_random_position()
        self.size = [50, 50]
        self._enemy_speed_default = 10
        self.sprites = [
            self.pygame_engine.load_sprite_image(value)
            for key, value in vars(EnemyConstants).items()
            if not key.startswith("__")
        ]
        self.sprite_manager = SpriteManager(self.sprites, self.size)
        self.sprite = self.sprite_manager.current_sprite
        self.sprite = self.pygame_engine.scale_sprite(self.sprite, self.size[0], self.size[1])
        self._move_timer = 0
        self._move_interval = 0.5
        self._speed = Vector(0, 0)
        self.hitbox = Hitbox(self, Vector(1, 1), Vector(0, 0))
        self.shoot_interval = 1.5
        self.time_since_last_shot = 0
        self.spaceship_scalar_speed = 10
        self.direction_movimentation = DirectionMovimentationEnum.UP_SIDE.value
        self.sprite_manager.update_sprite(self.direction_movimentation)


    def change_move_timer(self, delta_time: float) -> None:
        self._move_timer += delta_time

        if self._move_timer >= self._move_interval:
            self._choose_new_direction()
            self._move_timer = 0


    def _choose_new_direction(self) -> None:
        random_direction = randint(0, 3)
        
        print(random_direction)

        if random_direction == DirectionMovimentationEnum.LEFT_SIDE.value:
            self.direction_movimentation = DirectionMovimentationEnum.LEFT_SIDE.value
        elif random_direction == DirectionMovimentationEnum.RIGHT_SIDE.value:
            self.direction_movimentation = DirectionMovimentationEnum.RIGHT_SIDE.value
        elif random_direction == DirectionMovimentationEnum.UP_SIDE.value:
            self.direction_movimentation = DirectionMovimentationEnum.UP_SIDE.value
        else:
            self.direction_movimentation = DirectionMovimentationEnum.DOWN_SIDE.value
        
        self.change_speed()
        self.update_sprite()
        
        
    def change_speed(self) -> None: 
               
        if self.direction_movimentation == DirectionMovimentationEnum.LEFT_SIDE.value:
            self._speed.x = -self.spaceship_scalar_speed
        elif self.direction_movimentation == DirectionMovimentationEnum.RIGHT_SIDE.value:
            self._speed.x = self.spaceship_scalar_speed
        elif self.direction_movimentation == DirectionMovimentationEnum.UP_SIDE.value:
            self._speed.y = -self.spaceship_scalar_speed
        else:
            self._speed.y = self.spaceship_scalar_speed

        self.sprite_manager.update_sprite(self.direction_movimentation)
        self.sprite = self.sprite_manager.current_sprite


    def update_sprite(self) -> None:
        self.sprite_manager.update_sprite(self.direction_movimentation)
        self.sprite = self.sprite_manager.current_sprite


    def physics_process(self, delta_time: float, screen_width: int, screen_height: int) -> None:
        super().physics_process(delta_time, screen_width, screen_height)
        self.hitbox.update()


    def _generate_random_position(self) -> Vector:
        max_x = 40
        max_y = 20
        spawn_x = randint(0, max_x)
        spawn_y = randint(0, max_y)
        return Vector(spawn_x, spawn_y)


    def shoot(self) -> Bullet:
        adjustment_position_x = None
        adjustment_position_y = None
        if self.direction_movimentation == DirectionMovimentationEnum.UP_SIDE.value:
            adjustment_position_x = self.position.x + 1
            adjustment_position_y = self.position.y + 2
        elif self.direction_movimentation == DirectionMovimentationEnum.LEFT_SIDE.value:
            adjustment_position_x = self.position.x + 2
            adjustment_position_y = self.position.y + 1
        elif self.direction_movimentation == DirectionMovimentationEnum.RIGHT_SIDE.value:
            adjustment_position_x = self.position.x
            adjustment_position_y = self.position.y + 1
        elif self.direction_movimentation == DirectionMovimentationEnum.DOWN_SIDE.value:
            adjustment_position_x = self.position.x + 1
            adjustment_position_y = self.position.y

        position_shoot = Vector(adjustment_position_x, adjustment_position_y)
        speed_shoot = Vector(0, 0)
        scalar_speed = 30
        delta = 3

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


    def update(self, delta_time):
        self.time_since_last_shot += delta_time
        if self.time_since_last_shot >= self.shoot_interval:
            self.time_since_last_shot = 0
        return None