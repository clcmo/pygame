from utils.helpers import get_messages

def draw_game_over(screen, language="en"):
    messages = get_messages(language)
    screen.clear()
    screen.draw.text(messages["game_over"], center=(400, 300), fontsize=60, color="red")
    screen.draw.text(messages["resume"], center=(400, 400), fontsize=40)
