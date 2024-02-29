from typing import Tuple

class Vector:

    def __init__(self) -> None:
        self.position_x: int = 0
        self.position_y: int = 0
    
    def set_position_x(self, position) -> None:
        self.position_x = position
        
    def get_position_x(self) -> int:
        return self.position_x
        
    def set_position_y(self, position) -> None:
        self.position_y = position
    
    def get_position_y(self) -> int:
        return self.position_y
    
    def get_final_position(self) -> Tuple[int]:
        return (self.position_x, self.position_y)