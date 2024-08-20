import pygame


class Hitbox:
    def __init__(self, object, width, height):
        self.object = object
        self.width = width
        self.height = height
        self.rect = pygame.Rect(
            object._position.x * object.pixel_to_meters,
            object._position.y * object.pixel_to_meters,
            width, height
        )

    def update(self):
        self.rect.x = self.object._position.x * self.object.pixel_to_meters
        self.rect.y = self.object._position.y * self.object.pixel_to_meters

    @staticmethod
    def check_collision(hitbox1, hitbox2):
        return hitbox1.rect.colliderect(hitbox2.rect)
