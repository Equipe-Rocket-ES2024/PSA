from src.library.vector.vector import Vector

class Object:

    def __init__(self):
        self._sprite: str = None
        self._position: Vector = None
        self._speed: Vector = None
        self._size = 0
        self.pixel_to_meters = 0
