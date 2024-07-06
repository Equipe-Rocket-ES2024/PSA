from src.library.vector.vector import Vector

class Object:

    def __init__(self):
        self._sprite: str = None
        self._size = 0
        self._speed = Vector(0, 0)
        self._position = Vector(0, 0)
        self.pixel_to_meters = 0

    def physics_proccess(self, delta_time: float, screen_width: int, screen_height: int) -> None:
        # Atualiza a posição baseada na velocidade e no tempo
        self._position.x += self._speed.x * delta_time
        self._position.y += self._speed.y * delta_time

        # Limita a posição dentro dos limites da tela
        if self._position.x < 0:
            self._position.x = 0
        elif self._position.x + self._size > screen_width:
            self._position.x = screen_width - self._size

        if self._position.y < 0:
            self._position.y = 0
        elif self._position.y + self._size > screen_height:
            self._position.y = screen_height - self._size