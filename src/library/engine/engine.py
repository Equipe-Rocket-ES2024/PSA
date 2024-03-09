from abc import ABC, abstractmethod


class Engine(ABC):
    
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def display_init(self):
        pass
    
    
    @abstractmethod
    def start_clock(self) -> None:
        pass