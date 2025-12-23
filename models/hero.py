from pygame import Rect
from utils.constants import HERO_SPEED

class Hero:
    def __init__(self, x, y):
        self.rect = Rect(x, y, 32, 32)
        self.direction = "down"
        self.sprite_index = 0
        self.speed = HERO_SPEED
        self.animation_timer = 0
        self.attacking = False

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        if dx > 0: self.direction = "right"
        elif dx < 0: self.direction = "left"
        elif dy > 0: self.direction = "down"
        elif dy < 0: self.direction = "up"

    def update_animation(self):
        self.animation_timer += 1
        if self.animation_timer >= 10:
            self.sprite_index = (self.sprite_index + 1) % 4
            self.animation_timer = 0

    def attack(self):
        self.attacking = True
