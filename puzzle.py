"""Interface gráfica (Tkinter) do jogo 2048.

Este módulo cria a janela do jogo, desenha o tabuleiro e trata o teclado.
As regras do jogo (movimentos, fusões e estado da partida) ficam em
``logic.py`` e as cores, fontes e teclas ficam em ``constants.py``.

Para jogar, execute::

    python3 puzzle.py
"""

from tkinter import Frame, Label, CENTER

import random

import logic

import constants as c


def gen():
    """Sorteia um índice válido (linha ou coluna) do tabuleiro."""
    return random.randint(0, c.GRID_LEN - 1)


class GameGrid(Frame):
    """Janela principal do jogo.

    Atributos:
        commands: dicionário que associa cada tecla de movimento à função
            correspondente de ``logic`` (up, down, left, right).
        grid_cells: matriz de Labels, uma por célula do tabuleiro.
        matrix: estado atual do tabuleiro (lista de listas de inteiros).
        history_matrixs: estados anteriores, usados pelo desfazer (tecla B).
        moves: quantidade de jogadas válidas da partida atual.
        moves_label: Label que exibe o contador de movimentos.
    """

    def __init__(self):
        """Monta a janela, cria o tabuleiro e inicia o laço de eventos."""
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)

        self.commands = {
            c.KEY_UP: logic.up,
            c.KEY_DOWN: logic.down,
            c.KEY_LEFT: logic.left,
            c.KEY_RIGHT: logic.right,
            c.KEY_UP_ALT1: logic.up,
            c.KEY_DOWN_ALT1: logic.down,
            c.KEY_LEFT_ALT1: logic.left,
            c.KEY_RIGHT_ALT1: logic.right,
            c.KEY_UP_ALT2: logic.up,
            c.KEY_DOWN_ALT2: logic.down,
            c.KEY_LEFT_ALT2: logic.left,
            c.KEY_RIGHT_ALT2: logic.right,
        }

        self.grid_cells = []
        # O contador precisa existir antes de init_grid, que cria o Label.
        self.moves = 0
        self.moves_label = None
        self.init_grid()
        self.matrix = logic.new_game(c.GRID_LEN)
        self.history_matrixs = []
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        """Cria os widgets: o contador de movimentos e as células do tabuleiro.

        O contador fica na linha 0 da janela e o tabuleiro na linha 1.
        """
        self.moves_label = Label(
            self,
            text="Movimentos: 0",
            font=c.FONT_MOVES,
            bg=c.BACKGROUND_COLOR_MOVES,
            fg=c.FOREGROUND_COLOR_MOVES,
            pady=c.MOVES_PADDING
        )
        self.moves_label.grid(row=0, column=0, sticky="ew")

        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME, width=c.SIZE, height=c.SIZE)
        background.grid(row=1, column=0)

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(
                    background,
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    width=c.SIZE / c.GRID_LEN,
                    height=c.SIZE / c.GRID_LEN
                )
                cell.grid(
                    row=i,
                    column=j,
                    padx=c.GRID_PADDING,
                    pady=c.GRID_PADDING
                )
                t = Label(
                    master=cell,
                    text="",
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    justify=CENTER,
                    font=c.FONT,
                    width=5,
                    height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def update_moves(self):
        """Atualiza o texto do contador com a quantidade atual de jogadas."""
        self.moves_label.configure(text="Movimentos: " + str(self.moves))

    def update_grid_cells(self):
        """Redesenha todas as células conforme o conteúdo de ``self.matrix``.

        Células com valor 0 ficam vazias; as demais mostram o número e usam
        as cores definidas em ``constants.py``.
        """
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number),
                        bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number]
                    )
        self.update_idletasks()

    def key_down(self, event):
        """Trata uma tecla pressionada.

        - Escape: encerra o programa.
        - B: desfaz a última jogada (e diminui o contador de movimentos).
        - Teclas de movimento: move as peças; se o tabuleiro mudou, sorteia
          uma nova peça, guarda o estado no histórico, soma 1 ao contador e
          verifica vitória ou derrota.
        """
        key = event.keysym
        print(event)
        if key == c.KEY_QUIT: exit()
        if key == c.KEY_BACK and len(self.history_matrixs) > 1:
            self.matrix = self.history_matrixs.pop()
            self.update_grid_cells()
            # Desfazer uma jogada também desfaz a contagem dela.
            self.moves = max(0, self.moves - 1)
            self.update_moves()
            print('back on step total step:', len(self.history_matrixs))
        elif key in self.commands:
            self.matrix, done = self.commands[key](self.matrix)
            if done:
                self.matrix = logic.add_two(self.matrix)
                # record last move
                self.history_matrixs.append(self.matrix)
                self.update_grid_cells()
                # Só conta a jogada se ela alterou o tabuleiro.
                self.moves += 1
                self.update_moves()
                if logic.game_state(self.matrix) == 'win':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if logic.game_state(self.matrix) == 'lose':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    def generate_next(self):
        """Coloca uma peça 2 em uma célula vazia sorteada (não usada no jogo)."""
        index = (gen(), gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (gen(), gen())
        self.matrix[index[0]][index[1]] = 2


game_grid = GameGrid()