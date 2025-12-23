# Python Roguelike/Platformer MVC Game

[![GitHub license](https://img.shields.io/github/license/clcmo/pygame?style=for-the-badge)](https://github.com/clcmo/pygame)
[![GitHub stars](https://img.shields.io/github/stars/clcmo/pygame?style=for-the-badge)](https://github.com/clcmo/pygame/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/clcmo/pygame?style=for-the-badge)](https://github.com/clcmo/pygame/network)
[![GitHub issues](https://img.shields.io/github/issues/clcmo/pygame?style=for-the-badge)](https://github.com/clcmo/pygame/issues)
[![GitHub donate](https://img.shields.io/github/sponsors/clcmo?color=pink&style=for-the-badge)](https://github.com/sponsors/clcmo)

Um jogo desenvolvido em **Python** utilizando **PgZero**, estruturado em arquitetura **MVC**.  
O projeto inclui menu principal, animações de sprites, inimigos com movimento próprio, sistema de vidas, progressão de níveis (até 3 fases), além de sons e música de fundo.

---

## 🎮 Começando

Essas instruções ajudarão você a obter uma cópia do projeto e executá-lo localmente.

### ✅ Pré-requisitos

- Sistema operacional: Windows, macOS ou Linux
- Python 3.8+  
- Biblioteca [PgZero](https://pygame-zero.readthedocs.io/en/stable/)  
- Módulos padrão: `math`, `random`  
- (Opcional) `pygame.Rect` para manipulação de colisões  

Instale PgZero com:

```bash
pip install pgzero
````

### ⚙️ Instalação

Clone este repositório:

```bash
git clone https://github.com/clcmo/pygame.git
````

Acesse a pasta do projeto:

```bash
cd pygame
````

Certifique-se de que os assets (sprites, sons e músicas) estão na pasta assets/.

### 🚀 Uso

Execute o jogo com:

```bash
pgzrun main.py
````

### 🎯 Mecânicas

- Menu principal: iniciar jogo, alternar sons/música, sair.
- Movimento: setas direcionais.
- Ataque: tecla SPACE.
- Pause: tecla P.
- Progressão: derrote todos inimigos para avançar até o nível 3.
- Vitória: ao completar o nível 3.
- Game Over: ao perder todas as vidas.

### 🤝 Contribuindo

Contribuições são bem-vindas!

- Faça um fork do projeto.
- Crie uma branch para sua feature (git checkout -b feature/nova-feature).
- Commit suas alterações (git commit -m 'Adiciona nova feature').
- Faça push para a branch (git push origin feature/nova-feature).
- Abra um Pull Request.

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
