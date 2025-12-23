# ============================================
# Global Game Constants
# ============================================

SCREEN = {
    "width": 800,
    "height": 600,
    "title": "Adventure Quest",
    "fps": 60,
    "icon_path": "assets/icons/game_icon.png",
    "background_image_path": "assets/images/background.png",
    "background_color": (0, 0, 0),  # RGB for black
    "font_name": "Arial",
    "font_size": 24,
}

MECHANIC = {
    "hero_speed": 5,
    "enemy_speed": 2,
    "initial_lives": 3,
    "max_levels": 3,
    "power_up_duration": 10,  # in seconds
    "score_per_enemy": 100,
    "bonus_score": 500,
}

CENTER = {
    "x": SCREEN["width"] // 2,
    "y": SCREEN["height"] // 2,
    "font_size": 48,
    "color": (255, 255, 255),  # RGB for white
    "duration": 3,  # in seconds
}

FILE = {
    "save": "savegame.dat",
    "high_scores": "highscores.dat",
    "log": "game.log",
}

VOLUME = {
    "music": 0.5,
    "effects": 0.7,
    "voice": 0.8,
    "mute": 0.0,
    "max": 1.0,
    "min": 0.0,
}

MODE = {
    "fullscreen": True,
    "windowed": False,
    "difficulty": "Normal",
    "easy": "Easy",
    "hard": "Hard",
}

CONTROLS_CONFIG = {
    "move_up": "UP_ARROW",
    "move_down": "DOWN_ARROW",
    "move_left": "LEFT_ARROW",
    "move_right": "RIGHT_ARROW",
    "shoot": "SPACE",
    "pause": "P",
    "resume": "R",
    "quit": "Q",
}

SUPPORTED_LANGUAGES = ["en", "pt"]
DEFAULT_LANGUAGE = "en"
