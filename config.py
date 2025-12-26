"""Game configuration and settings."""

# Game Difficulty Levels
DIFFICULTY_EASY = {
    "enemy_speed": 1,
    "hero_speed": 6,
    "initial_lives": 5,
    "enemy_health": 1,
    "power_up_chance": 0.3
}

DIFFICULTY_NORMAL = {
    "enemy_speed": 2,
    "hero_speed": 5,
    "initial_lives": 3,
    "enemy_health": 1,
    "power_up_chance": 0.2
}

DIFFICULTY_HARD = {
    "enemy_speed": 3,
    "hero_speed": 4,
    "initial_lives": 2,
    "enemy_health": 2,
    "power_up_chance": 0.1
}

# Default difficulty
DEFAULT_DIFFICULTY = "normal"

# Game Settings
GAME_SETTINGS = {
    "sound_enabled": True,
    "music_enabled": True,
    "language": "en",
    "fullscreen": False,
    "fps": 60,
    "debug_mode": False
}

# Level Configuration
LEVEL_CONFIG = {
    1: {
        "enemy_count": 2,
        "enemy_speed_multiplier": 1.0,
        "score_multiplier": 1.0
    },
    2: {
        "enemy_count": 3,
        "enemy_speed_multiplier": 1.2,
        "score_multiplier": 1.5
    },
    3: {
        "enemy_count": 4,
        "enemy_speed_multiplier": 1.5,
        "score_multiplier": 2.0
    }
}

# Animation Frame Rates
ANIMATION_SPEEDS = {
    "hero_idle": 0.2,
    "hero_moving": 0.1,
    "hero_attacking": 0.05,
    "enemy_idle": 0.2,
    "enemy_moving": 0.15,
    "enemy_defeated": 0.1
}

# Score Settings
SCORING = {
    "enemy_kill": 100,
    "level_complete": 500,
    "time_bonus": 10,
    "accuracy_bonus": 50
}

# Power-up Settings
POWER_UPS = {
    "health": {"duration": 5, "value": 1},
    "speed": {"duration": 8, "value": 1.5},
    "shield": {"duration": 10, "value": 1}
}

# Get difficulty settings
def get_difficulty_settings(difficulty=None):
    """Get difficulty settings by name."""
    if difficulty is None:
        difficulty = DEFAULT_DIFFICULTY
    
    difficulty_name = difficulty.lower()
    if difficulty_name == "easy":
        return DIFFICULTY_EASY
    elif difficulty_name == "hard":
        return DIFFICULTY_HARD
    else:
        return DIFFICULTY_NORMAL
