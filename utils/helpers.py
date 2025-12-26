def get_messages(language="en"):
    messages = {
        "en": {
            "title": "Game Title",
            "start": "Start Game",
            "settings": "Settings",
            "exit": "Exit",
            "pause": "Paused",
            "resume": "Resume",
            "score": "Score:",
            "lives": "Lives:",
            "victory": "Victory!",
            "game_over": "Game Over",
            "level": "Level {} Complete!"
        },
        "pt": {
            "title": "Título do Jogo",
            "start": "Iniciar Jogo",
            "settings": "Configurações",
            "exit": "Sair",
            "pause": "Pausado",
            "resume": "Continuar",
            "score": "Pontuação:",
            "lives": "Vidas:",
            "victory": "Vitória!",
            "game_over": "Fim de Jogo",
            "level": "Nível {} Completo!"
        }
    }
    return messages.get(language, messages["en"])