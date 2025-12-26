import pgzrun
from controllers.game_controller import GameController
from utils.constants import SCREEN

WIDTH = SCREEN["WIDTH"]
HEIGHT = SCREEN["HEIGHT"]

controller = GameController()

def draw():
    controller.draw()

def update(dt):
    controller.update(dt)

def on_mouse_down(pos):
    controller.on_mouse_down(pos)

def on_key_down(key):
    controller.on_key_down(key)

pgzrun.go()