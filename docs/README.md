# Jogo Python Roguelike/Plataforma MVC - PgZero

[![GitHub license](https://img.shields.io/github/license/clcmo/pygame?style=for-the-badge)](https://github.com/clcmo/pygame)
[![GitHub stars](https://img.shields.io/github/stars/clcmo/pygame?style=for-the-badge)](https://github.com/clcmo/pygame/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/clcmo/pygame?style=for-the-badge)](https://github.com/clcmo/pygame/network)
[![GitHub issues](https://img.shields.io/github/issues/clcmo/pygame?style=for-the-badge)](https://github.com/clcmo/pygame/issues)
[![GitHub donate](https://img.shields.io/github/sponsors/clcmo?color=pink&style=for-the-badge)](https://github.com/sponsors/clcmo)

Um jogo Python criado com PgZero (Pygame Zero) usando uma arquitetura **MVC**. Apresenta um sistema de menu totalmente funcional com **botões clicáveis**, personagem herói, inimigos com mecânica de patrulha, animações de sprites e um loop de jogo completo.

---

## Recursos implementados

✅ **Menu principal com botões clicáveis**

- Botão Iniciar jogo
- Botão Alternar som (status LIGADO/DESLIGADO)
- Botão Sair com efeitos de foco

✅ **Sistema de animação de sprites**

- Animações do herói (estados ocioso e em movimento)
- Animações dos inimigos (estados ocioso e em movimento)
- Quadros de animação baseados em cores para feedback visual

✅ **Mecânica do jogo**

- Movimento do herói (teclas de seta ou WASD)
- Sistema de ataque (barra de espaço)
- Sistema de patrulha inimiga com limites de zona
- Detecção de colisão
- Acompanhamento de vidas e pontuação
- Progressão de nível (até 3 níveis)

✅ **Sistema de interface do usuário**

- Classe de botão com detecção de hover e manipulação de clique
- HUD exibindo pontuação e vidas
- Funcionalidade do menu de pausa
- Gerenciamento do estado do jogo

✅ **Base de áudio**

- Gerenciador de áudio (pronto para integração de som)
- Alternância de som nas configurações do menu
- Espaço reservado para música de fundo e efeitos

## Estrutura do projeto

- `main.py` - Ponto de entrada PgZero com manipuladores de eventos
- `controllers/` - GameController e InputHandler
- `models/` - Lógica do jogo (Hero, Enemy, Level, GameState)
- `views/` - Renderização (MenuView, GameView, HUDView, PauseView)
- `utils/` - SpriteAnimation, Button, AudioManager, Constants, Helpers

## Executando o jogo

O jogo é executado através do fluxo de trabalho “Game” no modo VNC:

```bash
pgzrun main.py
```

## Controles

- **Teclas de seta ou WASD**: Movimento
- **Barra de espaço**: Ataque
- **P**: Pausar/Retomar
- **Mouse**: Navegação no menu

## Ficha técnica

- Python 3.11
- Bibliotecas: pgzero, pygame (apenas Rect, conforme permitido), math, random
- Arquitetura: Padrão MVC
- Resolução 800x600

## Conformidade

- ✅ Utiliza apenas bibliotecas aprovadas (PgZero, pygame Rect)
- ✅ Nomes claros em inglês e conformidade com PEP8
- ✅ Classes de animação de sprites adequadas
- ✅ Menu com botões clicáveis
- ✅ Estrutura do sistema de som
- ✅ Mecânica de patrulha inimiga e movimento do herói
- ✅ Loop de jogo completo com gerenciamento de estado

## Implementação recente (dezembro de 2025)

- Classe Button criada para interações com a interface do usuário
- Classe SpriteAnimation implementada com ciclo de quadros
- Menu funcional criado com detecção de cliques
- Adicionado tratamento de entradas para menus e estados do jogo
- Animações de heróis e inimigos integradas
- Chamadas do método de desenho PgZero corrigidas
- Saída VNC configurada para exibição na área de trabalho
