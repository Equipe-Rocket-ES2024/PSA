from src.library.vector.vector import Vector

class Object:

    def __init__(self):
        self._sprite: str = None
        self._size = 0
        self._speed = Vector(0, 0)
        self._position = Vector(0, 0)
        self.pixel_to_meters = 0

    def physics_proccess(self, delta_time: float) -> None:
        self._position.x += self._speed.x * delta_time
        self._position.y += self._speed.y * delta_time
