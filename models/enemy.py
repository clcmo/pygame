import random
from pygame import Rect
from utils.constants import ENEMY_SPEED

class Enemy:
    def __init__(self, x, y, territory):
        self.rect = Rect(x, y, 32, 32)
        self.territory = territory
        self.sprite_index = 0
        self.speed = ENEMY_SPEED
        self.animation_timer = 0
        self.alive = True

    def patrol(self):
        if self.alive:
            self.rect.x += random.choice([-self.speed, self.speed])
            self.rect.y += random.choice([-self.speed, self.speed])

    def update_animation(self):
        if self.alive:
            self.animation_timer += 1
            if self.animation_timer >= 15:
                self.sprite_index = (self.sprite_index + 1) % 4
                self.animation_timer = 0

    def defeat(self):
        self.alive = False
