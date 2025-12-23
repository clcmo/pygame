from pygame import Rect

class Hero:
    def __init__(self, x, y):
        self.rect = Rect(x, y, 32, 32)
        self.direction = "down"
        self.sprite_index = 0
        self.speed = 5
        self.animation_timer = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # Atualiza direção conforme movimento
        if dx > 0: self.direction = "right"
        elif dx < 0: self.direction = "left"
        elif dy > 0: self.direction = "down"
        elif dy < 0: self.direction = "up"

    def update_animation(self):
        # Incrementa timer e troca sprite a cada 10 ticks
        self.animation_timer += 1
        if self.animation_timer >= 10:
            self.sprite_index = (self.sprite_index + 1) % 4
            self.animation_timer = 0
