# Estrutura do Projeto Pygame

pygame/
│── main.py             # Controller
│── view.py             # View
│── model.py            # Gerencia estado geral do jogo
│── models/
│   ├── hero.py         # Classe Hero
│   └── enemy.py        # Classe Enemy
| -- views/
|    ├── menu.py        # Tela de Menu
|    └── game_over.py   # Tela de Game Over
|    ├── hero.py        # View do Heroi
|    └── enemy.py       # View do Inimigo
│── assets/
│   ├── images/         # Imagens do jogo
│   ├── sounds/         # Efeitos sonoros
│   └── music/          # Trilha sonora
│── levels/
│   ├── level1.py       # Definição do Nível 1
│   └── level2.py       # Definição do Nível 2
|   └── level3.py       # Definição do Nível Final
│── utils/
│   ├── helpers.py      # Funções auxiliares
│   └── constants.py    # Constantes do jogo
└── README.md           # Documentação do projeto

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
