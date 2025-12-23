from model import GameModel
import view

game = GameModel()

def update():
    game.update()
    game.hero.attacking = False  # ataque dura apenas 1 frame

def on_key_down(key):
    if game.state == "menu":
        if key == keys.S: game.state = "playing"
        elif key == keys.M: game.sound_on = not game.sound_on
        elif key == keys.E: exit()
    elif game.state == "playing":
        if key == keys.RIGHT: game.hero.move(game.hero.speed, 0)
        if key == keys.LEFT: game.hero.move(-game.hero.speed, 0)
        if key == keys.UP: game.hero.move(0, -game.hero.speed)
        if key == keys.DOWN: game.hero.move(0, game.hero.speed)
        if key == keys.SPACE: game.hero.attack()
        if key == keys.P: game.state = "paused"
    elif game.state in ["game_over", "victory"]:
        if key == keys.R: game.__init__()
    elif game.state == "paused":
        if key == keys.P: game.state = "playing"

def draw():
    view.draw(game.hero, game.enemies, game.state, game.hero_lives)

import pgzrun
pgzrun.go()
