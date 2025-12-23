import pgzrun
from utils.constants import SCREEN
from utils.helpers import get_messages
from views.menu import draw_menu
from views.game_over import draw_game_over
from views.hero import draw_hero
from views.enemy import draw_enemies
from views.power_up import draw_power_ups  # Assumindo que existe uma função para power_ups

def draw(hero, enemies, power_ups, score, lives, game_state, language="en"):
    screen.clear()
    screen.fill(SCREEN.get("background_color", (0, 0, 0)))
    messages = get_messages(language)
    if game_state == "menu":
        draw_menu(screen, language)
    elif game_state == "playing":
        draw_hero(screen, hero)
        draw_enemies(screen, enemies)
        draw_power_ups(screen, power_ups)
        screen.draw.text(f"{messages['lives_left'].format(lives)}", topleft=(10, 10), fontsize=30, color="white")
        screen.draw.text(f"{messages['score'].format(score)}", topright=(SCREEN["width"] - 10, 10), fontsize=30, color="white")
    elif game_state == "game_over":
        draw_game_over(screen, language)
    elif game_state == "victory":
        screen.draw.text(messages["victory"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2), fontsize=60, color="green")
        screen.draw.text(messages["resume"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2 + 100), fontsize=40)
    elif game_state == "paused":
        screen.draw.text(messages["pause"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2), fontsize=60, color="yellow")
        screen.draw.text(messages["resume"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2 + 100), fontsize=40)
    elif game_state == "instructions":
        screen.draw.text(messages["help"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2 - 100), fontsize=30)
    elif game_state == "settings":
        screen.draw.text(messages["settings"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2 - 200), fontsize=50)
        screen.draw.text(messages["sound_on"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2 - 100), fontsize=30)
        screen.draw.text(messages["difficulty"].format("Medium"), center=(SCREEN["width"] // 2, SCREEN["height"] // 2 - 50), fontsize=30)
    elif game_state == "high_scores":
        screen.draw.text(messages["high_scores"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2 - 200), fontsize=50)
        for i in range(5):
            screen.draw.text(f"{i+1}. Player{i+1} - {1000 - i*100}", center=(SCREEN["width"] // 2, SCREEN["height"] // 2 - 100 + i*40), fontsize=30)
    elif game_state == "pause_menu":
        screen.draw.text(messages["pause_menu"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2 - 100), fontsize=50)
        screen.draw.text(messages["resume"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2), fontsize=40)
        screen.draw.text(messages["exit_to_main_menu"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2 + 100), fontsize=40)
    elif game_state == "level_complete":
        screen.draw.text(f"{messages['level'].format(game.level)} Complete!", center=(SCREEN["width"] // 2, SCREEN["height"] // 2), fontsize=60, color="blue")
        screen.draw.text(messages["next_level"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2 + 100), fontsize=40)
    elif game_state == "loading":
        screen.draw.text(messages["loading"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2), fontsize=60)
    elif game_state == "saving":
        screen.draw.text(messages["saving"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2), fontsize=60)
    elif game_state == "cutscene":
        screen.draw.text(messages["cutscene"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2), fontsize=60)
    elif game_state == "tutorial":
        screen.draw.text(messages["tutorial"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2 - 200), fontsize=50)
        screen.draw.text(messages["help"], center=(SCREEN["width"] // 2, SCREEN["height"] // 2 - 100), fontsize=30)