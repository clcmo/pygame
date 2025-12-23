import random
from pygame import Rect

class Enemy:
    def __init__(self, x, y, territory):
        self.rect = Rect(x, y, 32, 32)
        self.territory = territory
        self.sprite_index = 0
        self.speed = 2
        self.animation_timer = 0

    def patrol(self):
        # Movimento aleatório simples
        self.rect.x += random.choice([-self.speed, self.speed])
        self.rect.y += random.choice([-self.speed, self.speed])

    def update_animation(self):
        self.animation_timer += 1
        if self.animation_timer >= 15:  # inimigos animam mais devagar
            self.sprite_index = (self.sprite_index + 1) % 4
            self.animation_timer = 0
