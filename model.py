from models.hero import Hero
from models.enemy import Enemy

class GameModel:
    def __init__(self):
        self.level = 1
        self.max_levels = 3
        self.hero = Hero(100, 100)
        self.enemies = self.create_enemies(self.level)
        self.state = "menu"
        self.sound_on = True
        self.hero_lives = 3
        self.victory = False

    def create_enemies(self, level):
        if level == 1:
            return [Enemy(200, 200, "zone1"), Enemy(400, 300, "zone2")]
        elif level == 2:
            return [Enemy(150, 150, "zone1"), Enemy(350, 250, "zone2"), Enemy(500, 400, "zone3")]
        elif level == 3:
            return [Enemy(100, 100, "zone1"), Enemy(300, 200, "zone2"), Enemy(500, 300, "zone3"), Enemy(600, 450, "zone4")]

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
                    sounds.attack.play()
                else:
                    self.hero_lives -= 1
                    if self.hero_lives <= 0:
                        self.state = "game_over"
                        sounds.hit.play()

    def check_victory(self):
        if all(not enemy.alive for enemy in self.enemies):
            if self.level < self.max_levels:
                self.state = "level_complete"
                sounds.victory.play()
            else:
                self.victory = True
                self.state = "victory"
                sounds.victory.play()

    def next_level(self):
        if self.level < self.max_levels:
            self.level += 1
            self.hero = Hero(100, 100)
            self.enemies = self.create_enemies(self.level)
            self.state = "playing"

    def play_music(level): music.stop() music.play(f"level{level}")

    def game_over(self):
        self.state = "game_over"
        sounds.game_over.play()
        music.stop()
        music.play("game_over")