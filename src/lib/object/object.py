from lib.vector.vector import Vector

class Object:

    def __init__(self):
        self.sprite: str = None
        self.position: Vector = None
        self.velocity: Vector = None
