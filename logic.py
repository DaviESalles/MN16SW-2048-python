"""Regras do jogo 2048.

O tabuleiro é uma matriz (lista de listas de inteiros) em que 0 representa
uma célula vazia. Todas as funções de movimento (``up``, ``down``, ``left``
e ``right``) recebem a matriz e retornam uma tupla ``(nova_matriz, mudou)``,
em que ``mudou`` indica se a jogada alterou o tabuleiro.

Todos os movimentos reutilizam a lógica de "mover para a esquerda":
para os demais sentidos, a matriz é transposta e/ou invertida, movida para
a esquerda e depois desfeita.
"""

#
# CS1010FC --- Programming Methodology
#
# Mission N Solutions
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import random

import constants as c


def new_game(n):
    """Cria um tabuleiro n x n zerado e sorteia duas peças iniciais (valor 2)."""
    matrix = []

    for i in range(n):
        matrix.append([0] * n)
    matrix = add_two(matrix)
    matrix = add_two(matrix)
    return matrix


def add_two(mat):
    """Coloca uma peça de valor 2 em uma célula vazia sorteada.

    Sorteia posições até encontrar uma célula com valor 0, portanto o
    tabuleiro precisa ter ao menos uma célula vazia. Retorna a própria
    matriz modificada.
    """
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    while mat[a][b] != 0:
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    mat[a][b] = 2
    return mat


def game_state(mat):
    """Informa a situação da partida.

    A verificação segue esta ordem:
      1. Se existe alguma peça 2048, retorna 'win'.
      2. Se existe alguma célula vazia, retorna 'not over'.
      3. Se existem duas peças iguais vizinhas (linha ou coluna), ainda há
         fusão possível e retorna 'not over'.
      4. Caso contrário, retorna 'lose'.

    O terceiro passo percorre o tabuleiro comparando cada célula com a da
    direita e a de baixo; a última linha e a última coluna são tratadas à
    parte para não sair dos limites da matriz.
    """
    # check for win cell
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'

    # check for any zero entries
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'

    # check for same cells that touch each other
    for i in range(len(mat)-1):
        # intentionally reduced to check the row on the right and below
        # more elegant to use exceptions but most likely this will be their solution
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
    for k in range(len(mat)-1):  # to check the left/right entries on the last row
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'not over'

    for j in range(len(mat)-1):  # check up/down entries on last column
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'not over'

    return 'lose'


def reverse(mat):
    """Inverte cada linha da matriz (espelha na horizontal).

    Retorna uma nova matriz, sem alterar a original.
    """
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new


def transpose(mat):
    """Transpõe a matriz (linhas viram colunas e vice-versa).

    Retorna uma nova matriz, sem alterar a original.
    """
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new


def cover_up(mat):
    """Empurra todas as peças de cada linha para a esquerda, sem fundi-las.

    Para cada linha, copia as peças diferentes de zero para o início de uma
    linha nova, mantendo a ordem. Usa ``c.GRID_LEN`` como tamanho do
    tabuleiro.

    Retorna ``(nova_matriz, done)``, em que ``done`` é True se alguma peça
    mudou de posição.
    """
    new = []
    for j in range(c.GRID_LEN):
        partial_new = []
        for i in range(c.GRID_LEN):
            partial_new.append(0)
        new.append(partial_new)
    done = False
    for i in range(c.GRID_LEN):
        count = 0
        for j in range(c.GRID_LEN):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done


def merge(mat, done):
    """Funde peças iguais vizinhas em cada linha, da esquerda para a direita.

    Quando duas peças iguais (e diferentes de zero) se encontram, a primeira
    passa a valer o dobro e a segunda vira 0. A matriz é alterada no lugar.

    Args:
        mat: matriz já compactada à esquerda por ``cover_up``.
        done: valor anterior do indicador de mudança.

    Retorna ``(matriz, done)``, com ``done`` True se houve alguma fusão ou se
    já era True.
    """
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN-1):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
    return mat, done


def up(game):
    """Move as peças para cima (transpõe, move à esquerda e desfaz)."""
    print("up")
    # return matrix after shifting up
    game = transpose(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(game)
    return game, done


def down(game):
    """Move as peças para baixo (transpõe e inverte, move à esquerda e desfaz)."""
    print("down")
    # return matrix after shifting down
    game = reverse(transpose(game))
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return game, done


def left(game):
    """Move as peças para a esquerda: compacta, funde e compacta de novo."""
    print("left")
    # return matrix after shifting left
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    return game, done


def right(game):
    """Move as peças para a direita (inverte, move à esquerda e desfaz)."""
    print("right")
    # return matrix after shifting right
    game = reverse(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = reverse(game)
    return game, done