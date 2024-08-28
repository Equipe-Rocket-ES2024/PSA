from src.library.vector.vector import Vector

class Object:

    def __init__(self):
        self._sprite: str = None
        self.size = [0, 0]
        self._speed = Vector(0, 0)
        self.position = Vector(0, 0)
        self.pixel_to_meters = 0

    def physics_process(self, delta_time: float, screen_width: int, screen_height: int) -> None:
        new_x = self.position.x + self._speed.x * delta_time
        new_y = self.position.y + self._speed.y * delta_time

        if new_x < 0:
            new_x = 0
        elif new_x + self.size[0] > screen_width:
            new_x = screen_width - self.size[0]
        
        if new_y < 0:
            new_y = 0
        elif new_y + self.size[1] > screen_height:  
            new_y = screen_height - self.size[1]
        
        self.position.x = new_x
        self.position.y = new_y
