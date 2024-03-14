from src.library.engine.engine import Engine
import pygame


class PygameEngine(Engine):
    
    def __init__(self) -> None:
        pass
    
    def display_init(self) -> None:
        return pygame.display.init()
    
    def start_clock(self) -> int:
        return pygame.time.Clock()
    
    def display_quit(self) -> None:
        return pygame.quit()