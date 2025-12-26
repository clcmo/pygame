from pygame import Rect
from utils.constants import ENEMY_SPEED

class Enemy:
    def __init__(self, x, y, zone):
        self.x = x
        self.y = y
        self.speed = ENEMY_SPEED
        self.zone = zone
        self.alive = True
        self.rect = Rect(self.x, self.y, 32, 32)  # Placeholder para sprite

    def patrol(self):
        # Lógica simples de patrulha
        if self.zone == "zone1":
            self.x += self.speed
            if self.x > 400: self.speed = -self.speed
            if self.x < 200: self.speed = -self.speed
        self.rect.topleft = (self.x, self.y)

    def defeat(self):
        self.alive = False

    def update_animation(self):
        # Placeholder para animação
        pass