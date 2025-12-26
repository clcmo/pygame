from views.base_view import BaseView
from utils.constants import SCREEN

class GameView(BaseView):
    def draw(self, screen, hero, enemies, power_ups):
        screen.fill((0, 0, 0))
        # Desenhar herói
        screen.draw.rect(hero.rect, "blue")
        # Desenhar inimigos
        for enemy in enemies:
            if enemy.alive:
                screen.draw.rect(enemy.rect, "red")
        # Desenhar power-ups
        for power_up in power_ups:
            screen.draw.circle(power_up["pos"], 10, "yellow")