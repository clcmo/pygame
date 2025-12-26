import pgzrun

class InputHandler:
    def __init__(self, controller):
        self.controller = controller

    def handle_mouse(self, pos):
        # Lógica para cliques (ex.: botões no menu)
        pass

    def handle_key(self, key):
        if self.controller.game_state.state == "menu":
            if key == keys.S:
                self.controller.game_state.state = "playing"
            elif key == keys.E:
                exit()
        elif self.controller.game_state.state == "playing":
            if key == keys.RIGHT:
                self.controller.hero.move(self.controller.hero.speed, 0)
            elif key == keys.LEFT:
                self.controller.hero.move(-self.controller.hero.speed, 0)
            elif key == keys.UP:
                self.controller.hero.move(0, -self.controller.hero.speed)
            elif key == keys.DOWN:
                self.controller.hero.move(0, self.controller.hero.speed)
            elif key == keys.SPACE:
                self.controller.hero.attack()
            elif key == keys.P:
                self.controller.game_state.state = "paused"
        elif self.controller.game_state.state == "paused":
            if key == keys.P:
                self.controller.game_state.state = "playing"