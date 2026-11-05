# 2048 Python

Versão em Python do jogo [2048](https://github.com/gabrielecirulli/2048), de Gabriele Cirulli, com interface gráfica em Tkinter.

Este repositório é um fork de [yangshun/2048-python](https://github.com/yangshun/2048-python) e é usado no trabalho de manutenção de software da disciplina MN16SW (UTFPR-DV).

![screenshot](img/screenshot.png)

## Como jogar

O objetivo é deslizar as peças numeradas pelo tabuleiro para combiná-las até formar a peça **2048**. Quando duas peças com o mesmo número se encontram, elas se fundem em uma só com a soma dos valores. A cada jogada que move o tabuleiro surge uma nova peça de valor 2. Se o tabuleiro encher e não houver mais fusões possíveis, o jogo termina.

| Tecla | Ação |
|---|---|
| Setas | Mover as peças |
| W, A, S, D | Mover as peças (cima, esquerda, baixo, direita) |
| I, J, K, L | Mover as peças (cima, esquerda, baixo, direita) |
| B | Desfazer a última jogada |
| Esc | Sair do jogo |

O contador **Movimentos**, acima do tabuleiro, mostra quantas jogadas válidas foram feitas na partida atual. Jogadas que não alteram o tabuleiro não são contadas, e desfazer uma jogada diminui o contador.

## Requisitos

- Python 3
- Tkinter (já vem com o Python no Windows e no macOS; no Linux, instale com `sudo apt install python3-tk`)

## Como executar

```bash
git clone https://github.com/DaviESalles/MN16SW-2048-python.git
cd MN16SW-2048-python
python3 puzzle.py
```

## Estrutura do projeto

| Arquivo | Descrição |
|---|---|
| `puzzle.py` | Interface gráfica: janela, tabuleiro, contador de movimentos e tratamento do teclado |
| `logic.py` | Regras do jogo: criação do tabuleiro, movimentos, fusões e estado da partida (`win`, `lose`, `not over`) |
| `constants.py` | Tamanho do tabuleiro, cores, fontes e teclas |

## Como o jogo funciona

O tabuleiro é uma matriz em que `0` representa uma célula vazia. Cada movimento segue três passos: compactar as peças para um lado, fundir as peças iguais vizinhas e compactar de novo. Para mover em qualquer sentido, o código reaproveita o movimento para a esquerda, transpondo e/ou invertendo a matriz antes e depois.

## Contribuidores

- [Yanghun Tay](http://github.com/yangshun) e [Emmanuel Goh](http://github.com/emman27), autores do projeto original
- Equipe do trabalho de manutenção (UTFPR-DV)