from views.base_view import BaseView
from utils.constants import SCREEN

class MenuView(BaseView):
    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.draw_text(screen, "title", (SCREEN["WIDTH"] // 2, 100), fontsize=60)
        self.draw_text(screen, "start", (SCREEN["WIDTH"] // 2, 300), fontsize=40)
        self.draw_text(screen, "settings", (SCREEN["WIDTH"] // 2, 400), fontsize=40)
        self.draw_text(screen, "exit", (SCREEN["WIDTH"] // 2, 500), fontsize=40)