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


    def change_speed(self, delta_time: float) -> None:
        self._move_timer += delta_time

        if self._move_timer >= self._move_interval:
            self._choose_new_direction()
            self._move_timer = 0


    def _choose_new_direction(self) -> None:
        self._speed.x = uniform(
            -self._enemy_speed_default,
            self._enemy_speed_default
        )
        self._speed.y = uniform(
            -self._enemy_speed_default,
            self._enemy_speed_default
        )
        self.update_sprite()


    def update_sprite(self) -> None:
        if self._speed.x > 0 and self._speed.y == 0:
            self.sprite = self.sprites[0]  # direita
        elif self._speed.x < 0 and self._speed.y == 0:
            self.sprite = self.sprites[1]  # esquerda
        elif self._speed.y > 0 and self._speed.x == 0:
            self.sprite = self.sprites[2]  # baixo
        elif self._speed.y < 0 and self._speed.x == 0:
            self.sprite = self.sprites[3]  # cima
        elif self._speed.x > 0 and self._speed.y > 0:
            # Movimento diagonal para baixo-direita
            # Aqui você pode escolher um sprite que represente essa direção diagonal
            self.sprite = self.sprites[2]  # Por exemplo, usando o sprite de movimento para baixo
        elif self._speed.x > 0 and self._speed.y < 0:
            # Movimento diagonal para cima-direita
            self.sprite = self.sprites[0]  # Usando o sprite de movimento para a direita
        elif self._speed.x < 0 and self._speed.y > 0:
            # Movimento diagonal para baixo-esquerda
            self.sprite = self.sprites[2]  # Usando o sprite de movimento para baixo
        elif self._speed.x < 0 and self._speed.y < 0:
            # Movimento diagonal para cima-esquerda
            self.sprite = self.sprites[3]  # Usando o sprite de movimento para cima

        self.sprite = self.pygame_engine.scale_sprite(
            self.sprite, self.size[0], self.size[1]
        )


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
        position = Vector(self.position.x + 1, self.position.y + 3)
        return Bullet(self.screen, position, 30)


    def update(self, delta_time):
        self.time_since_last_shot += delta_time
        if self.time_since_last_shot >= self.shoot_interval:
            self.time_since_last_shot = 0
        return None