from models.hero import Hero
from models.enemy import Enemy

class GameModel:
    def __init__(self):
        self.hero = Hero(100, 100)
        self.enemies = [
            Enemy(200, 200, "zone1"),
            Enemy(400, 300, "zone2")
        ]
        self.state = "menu"
        self.sound_on = True
        self.hero_lives = 3
        self.victory = False

    def update(self):
        if self.state == "playing" and not self.victory:
            for enemy in self.enemies:
                enemy.patrol()
                enemy.update_animation()
            self.hero.update_animation()
            self.check_collisions()
            self.check_victory()

    def check_collisions(self):
        for enemy in self.enemies:
            if enemy.alive and self.hero.rect.colliderect(enemy.rect):
                if self.hero.attacking:
                    enemy.defeat()
                else:
                    self.hero_lives -= 1
                    if self.hero_lives <= 0:
                        self.state = "game_over"

    def check_victory(self):
        # Vitória se todos inimigos forem derrotados
        if all(not enemy.alive for enemy in self.enemies):
            self.victory = True
            self.state = "victory"
