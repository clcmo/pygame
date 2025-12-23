from utils.helpers import get_messages

def draw_menu(screen, language="en"):
    messages = get_messages(language)
    screen.clear()
    screen.draw.text(messages["welcome"], center=(400, 100), fontsize=50)
    screen.draw.text(messages["start_game"], center=(400, 200), fontsize=40)
    screen.draw.text(messages["help"], center=(400, 300), fontsize=30)
    screen.draw.text(messages["exit"], center=(400, 400), fontsize=40)
