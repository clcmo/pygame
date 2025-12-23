import pgzrun

WIDTH = 800
HEIGHT = 600

def draw(hero, enemies, game_state, lives):
    screen.clear()
    if game_state == "menu":
        screen.draw.text("Start Game", center=(400, 200), fontsize=40)
        screen.draw.text("Toggle Sound", center=(400, 300), fontsize=40)
        screen.draw.text("Exit", center=(400, 400), fontsize=40)
    elif game_state == "playing":
        # Hero
        screen.blit(f"hero_{hero.direction}{hero.sprite_index}", (hero.rect.x, hero.rect.y))
        # Enemies
        for enemy in enemies:
            screen.blit(f"enemy{enemy.sprite_index}", (enemy.rect.x, enemy.rect.y))
        # HUD com vidas
        screen.draw.text(f"Lives: {lives}", topleft=(10, 10), fontsize=30, color="white")
    elif game_state == "game_over":
        screen.draw.text("GAME OVER", center=(400, 300), fontsize=60, color="red")
        screen.draw.text("Press R to Restart", center=(400, 400), fontsize=40)
    elif game_state == "victory":
        screen.draw.text("YOU WIN!", center=(400, 300), fontsize=60, color="green")
        screen.draw.text("Press R to Restart", center=(400, 400), fontsize=40)
    elif game_state == "paused":
        screen.draw.text("PAUSED", center=(400, 300), fontsize=60, color="yellow")
        screen.draw.text("Press P to Resume", center=(400, 400), fontsize=40)
    elif game_state == "instructions":
        screen.draw.text("Instructions", center=(400, 100), fontsize=50)
        screen.draw.text("Use arrow keys to move", center=(400, 200), fontsize=30)
        screen.draw.text("Avoid enemies and survive", center=(400, 250), fontsize=30)
        screen.draw.text("Press I to go back", center=(400, 400), fontsize=40)
    elif game_state == "settings":
        screen.draw.text("Settings", center=(400, 100), fontsize=50)
        screen.draw.text("Sound: On/Off", center=(400, 200), fontsize=30)
        screen.draw.text("Difficulty: Easy/Medium/Hard", center=(400, 250), fontsize=30)
        screen.draw.text("Press S to go back", center=(400, 400), fontsize=40)
    elif game_state == "high_scores":
        screen.draw.text("High Scores", center=(400, 100), fontsize=50)
        # Placeholder for high scores
        for i in range(5):
            screen.draw.text(f"{i+1}. Player{i+1} - {1000 - i*100}", center=(400, 200 + i*40), fontsize=30)
        screen.draw.text("Press H to go back", center=(400, 400), fontsize=40)
    elif game_state == "pause_menu":
        screen.draw.text("Pause Menu", center=(400, 200), fontsize=50)
        screen.draw.text("Resume Game", center=(400, 300), fontsize=40)
        screen.draw.text("Exit to Main Menu", center=(400, 400), fontsize=40)
    elif game_state == "level_complete":
        screen.draw.text("Level Complete!", center=(400, 300), fontsize=60, color="blue")
        screen.draw.text("Press N for Next Level", center=(400, 400), fontsize=40)
    elif game_state == "loading":
        screen.draw.text("Loading...", center=(400, 300), fontsize=60)
    elif game_state == "saving":
        screen.draw.text("Saving Game...", center=(400, 300), fontsize=60)
    elif game_state == "cutscene":
        screen.draw.text("Cutscene Playing...", center=(400, 300), fontsize=60)
    elif game_state == "tutorial":
        screen.draw.text("Tutorial", center=(400, 100), fontsize=50)
        screen.draw.text("Learn the basics of the game", center=(400, 200), fontsize=30)
        screen.draw.text("Press T to go back", center=(400, 400), fontsize=40)