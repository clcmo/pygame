from pygame import Rect
from utils.constants import HERO_SPEED

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = HERO_SPEED
        self.alive = True
        self.attacking = False
        self.rect = Rect(self.x, self.y, 32, 32)  # Placeholder para sprite

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.topleft = (self.x, self.y)

    def attack(self):
        self.attacking = True

    def update_animation(self):
        # Placeholder para animação
        pass