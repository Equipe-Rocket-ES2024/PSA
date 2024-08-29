from src.library.vector.vector import Vector

class Object:

    def __init__(self):
        self.sprite: str = None
        self.size = [0, 0]
        self._speed = Vector(0, 0)
        self.position = Vector(0, 0)
        self.meters_to_pixel = 10


    def physics_process(self, delta_time: float, screen_width: int, screen_height: int) -> None:
        max_x = (screen_width / self.meters_to_pixel) - self.size[0]
        max_y = (screen_height / self.meters_to_pixel) - self.size[1]

        max_x = max(0, max_x)
        max_y = max(0, max_y)

        self.position.x += self._speed.x * delta_time
        self.position.y += self._speed.y * delta_time

        self.position.x = max(0, min(self.position.x, max_x))
        self.position.y = max(0, min(self.position.y, max_y))

        print(f"Posição: {self.position}, Limite X: {max_x}, Limite Y: {max_y}")


    def draw_object(self, screen) -> None:
        screen.blit(self.sprite, (self.position.x *
                         self.meters_to_pixel, self.position.y * self.meters_to_pixel))
