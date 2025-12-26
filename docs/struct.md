# Estrutura do Projeto Pygame

pygame/
├── main.py                  # Ponto de entrada PgZero
│
├── models/                  # MODEL - lógica e estado
│   ├── __init__.py
│   ├── game_state.py        # Estado global do jogo
│   ├── hero.py              # Classe do herói
│   ├── enemy.py             # Classe dos inimigos
│   └── level.py             # Cenário e lógica de mapa
│
├── views/                   # VIEW - renderização e UI
│   ├── __init__.py
│   ├── base_view.py         # Classe base para telas
│   ├── menu_view.py         # Tela de menu principal
│   ├── game_view.py         # Tela do jogo
│   ├── pause_view.py        # Tela de pausa
│   └── hud_view.py          # Interface HUD (vida, score)
│
├── controllers/             # CONTROLLER - input e fluxo
│   ├── __init__.py
│   ├── game_controller.py   # Controlador principal
│   └── input_handler.py     # Gerenciamento de cliques/teclas
│
├── assets/                  # Sprites e sons (pack Kenney)
│   ├── sprites/
│   │   ├── hero/
│   │   ├── enemies/
│   │   └── ui/              # Botões sci-fi do Kenney
│   └── sounds/
│       ├── effects/
│       └── music/
│
└── utils/                   # Utilitários
    ├── __init__.py
    ├── animations.py         # Ciclo de sprites
    ├── audio_manager.py      # Música e efeitos
    └── constants.py          # Constantes globais

## Descrição dos Componentes

- `main.py`: Ponto de entrada do jogo, responsável por iniciar o loop principal e coordenar a interação entre o modelo e a visão.
- `view.py`: Gerencia a renderização gráfica e a interface do usuário.
- `model.py`: Mantém o estado geral do jogo, incluindo pontuação, vidas e progresso.
- `models/`: Contém as classes que representam os personagens e objetos do jogo, como o herói e os inimigos.
- `assets/`: Diretório que armazena todos os recursos multimídia necessários para o jogo, como imagens, sons e música.
- `levels/`: Define os diferentes níveis do jogo, incluindo layout, inimigos e desafios específicos.
- `utils/`: Contém funções auxiliares e constantes que são usadas em várias partes do código para facilitar a manutenção e a legibilidade.
- `README.md`: Fornece uma visão geral do projeto, instruções de instalação e informações relevantes para desenvolvedores e usuários.

Esta estrutura modular facilita a organização do código, tornando-o mais fácil de manter e expandir conforme o desenvolvimento do jogo avança.
