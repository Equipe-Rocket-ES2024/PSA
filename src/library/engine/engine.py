from abc import ABC, abstractmethod


class Engine(ABC):
    
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def display_init(self):
        pass
    
    @abstractmethod
    def start_clock(self) -> int:
        pass
    
    @abstractmethod
    def display_quit(self) -> None:
        pass
    
    @abstractmethod
    def display_flip(self) -> None:
        pass
