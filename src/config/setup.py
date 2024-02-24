import pygame

class Setup:
    
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0, 0 , 0)
        self.game_name = "Star wars X Star Treek"
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption(self.game_name)
