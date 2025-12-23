# Visual Game Constants

# Screen Constants
WIDTH = 800
HEIGHT = 600
HERO_SPEED = 5
ENEMY_SPEED = 2
INITIAL_LIVES = 3
MAX_LEVELS = 3
POWER_UP_DURATION = 10  # in seconds
SCORE_PER_ENEMY = 100
BONUS_SCORE = 500
BACKGROUND_COLOR = (0, 0, 0)  # RGB for black
FONT_NAME = "Arial"
FONT_SIZE = 24

# Game Constants
SAVE_FILE = "savegame.dat"
HIGH_SCORE_FILE = "highscores.dat"
LOG_FILE = "game.log"
DEFAULT_VOLUME = 0.5  # Volume level from 0.0 to 1.0
MUTE_VOLUME = 0.0
MAX_VOLUME = 1.0
MIN_VOLUME = 0.0
FULLSCREEN_MODE = False
WINDOWED_MODE = True
DEFAULT_DIFFICULTY = "Normal"
EASY_DIFFICULTY = "Easy"
HARD_DIFFICULTY = "Hard"

# Controls Constants
CONTROLS_CONFIG = {
    "move_up": "UP_ARROW",
    "move_down": "DOWN_ARROW",
    "move_left": "LEFT_ARROW",
    "move_right": "RIGHT_ARROW",
    "shoot": "SPACE",
    "pause": "P",
    "resume": "R",
    "quit": "Q"
}

# Messages Constants and Translations
SUPPORTED_LANGUAGES = ["en", "pt"]
DEFAULT_LANGUAGE = "en"
WELCOME_MESSAGE = "Welcome to the Game!"
GAME_OVER_MESSAGE = "Game Over!"
LEVEL_UP_MESSAGE = "Level Up!"
VICTORY_MESSAGE = "You Win!"
PAUSE_MESSAGE = "Game Paused"
RESUME_MESSAGE = "Resuming Game"
POWER_UP_MESSAGE = "Power Up Activated!"
LIVES_LEFT_MESSAGE = "Lives Left: {}"
SCORE_MESSAGE = "Score: {}"
LEVEL_MESSAGE = "Level: {}"
EXIT_MESSAGE = "Thanks for playing!"
HELP_MESSAGE = "Use arrow keys to move, space to shoot."
ERROR_MESSAGE = "An error occurred. Please try again."

TRANSLATIONS = {
    "en": {
        "welcome": WELCOME_MESSAGE,
        "game_over": GAME_OVER_MESSAGE,
        "level_up": LEVEL_UP_MESSAGE,
        "victory": VICTORY_MESSAGE,
        "pause": PAUSE_MESSAGE,
        "resume": RESUME_MESSAGE,
        "power_up": POWER_UP_MESSAGE,
        "lives_left": LIVES_LEFT_MESSAGE,
        "score": SCORE_MESSAGE,
        "level": LEVEL_MESSAGE,
        "exit": EXIT_MESSAGE,
        "help": HELP_MESSAGE,
        "error": ERROR_MESSAGE
    },
    "pt": {
        "welcome": "Bem-vindo ao Jogo!",
        "game_over": "Fim de Jogo!",
        "level_up": "Subiu de Nível!",
        "victory": "Você Venceu!",
        "pause": "Jogo Pausado",
        "resume": "Retomar Jogo",
        "power_up": "Power Up Ativado!",
        "lives_left": "Vidas Restantes: {}",
        "score": "Pontuação: {}",
        "level": "Nível: {}",
        "exit": "Obrigado por jogar!",
        "help": "Use as setas para mover, espaço para atirar.",
        "error": "Ocorreu um erro. Por favor, tente novamente."
    }
}