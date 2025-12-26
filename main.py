import pgzrun
from controllers.game_controller import GameController
from utils.constants import SCREEN

WIDTH = SCREEN["WIDTH"]
HEIGHT = SCREEN["HEIGHT"]

controller = GameController()
mouse_pos = (0, 0)

def draw():
    controller.draw(screen)
    if controller.game_state.state == "menu":
        controller.views["menu"].update(mouse_pos)

def update(dt):
    controller.update(dt)

def on_mouse_down(pos):
    controller.on_mouse_down(pos)

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def on_key_down(key):
    controller.on_key_down(key)

pgzrun.go()
