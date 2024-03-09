from typing import Tuple

class Vector:

    def __init__(self) -> None:
        self.x: float = 0
        self.y: float = 0
    
    def set_x(self, x) -> None:
        self.x = x
        
    def get_x(self) -> float:
        return self.x
        
    def set_y(self, position) -> None:
        self.y = position
    
    def get_y(self) -> float:
        return self.y
    
    def get_tuple(self) -> Tuple[float]:
        return (self.x, self.y)