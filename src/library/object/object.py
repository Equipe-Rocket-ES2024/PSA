from src.library.vector.vector import Vector

class Object:

    def __init__(self):
        self._sprite: str = None
        self._size = 0
        self._speed = Vector(0, 0)
        self._position = Vector(0, 0)
        self.pixel_to_meters = 0

    def physics_process(self, delta_time: float, screen_width: int, screen_height: int) -> None:
        new_x = self._position.x + self._speed.x * delta_time
        new_y = self._position.y + self._speed.y * delta_time

        if new_x < 0:
            new_x = 0
        elif new_x + self._size > screen_width:
            new_x = screen_width - self._size
        
        if new_y < 0:
            new_y = 0
        elif new_y + self._size > screen_height:
            new_y = screen_height - self._size
        
        self._position.x = new_x
        self._position.y = new_y
