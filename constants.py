"""Constantes do jogo 2048: tamanho, cores, fontes e teclas.

Centraliza os valores usados por ``puzzle.py`` (interface) e ``logic.py``
(regras), para que possam ser ajustados em um único lugar.
"""

# --- Tabuleiro ---------------------------------------------------------
SIZE = 400          # tamanho do tabuleiro em pixels (largura e altura)
GRID_LEN = 4        # número de linhas e colunas do tabuleiro
GRID_PADDING = 10   # espaço, em pixels, entre as células

# --- Cores do tabuleiro ------------------------------------------------
BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"

# Cor de fundo de cada célula, conforme o valor da peça.
BACKGROUND_COLOR_DICT = {
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e",
    4096: "#eee4da",
    8192: "#edc22e",
    16384: "#f2b179",
    32768: "#f59563",
    65536: "#f67c5f",
}

# Cor do número de cada célula, conforme o valor da peça.
CELL_COLOR_DICT = {
    2: "#776e65",
    4: "#776e65",
    8: "#f9f6f2",
    16: "#f9f6f2",
    32: "#f9f6f2",
    64: "#f9f6f2",
    128: "#f9f6f2",
    256: "#f9f6f2",
    512: "#f9f6f2",
    1024: "#f9f6f2",
    2048: "#f9f6f2",
    4096: "#776e65",
    8192: "#f9f6f2",
    16384: "#776e65",
    32768: "#776e65",
    65536: "#f9f6f2",
}

# --- Fontes ------------------------------------------------------------
FONT = ("Verdana", 40, "bold")        # números das peças

# --- Contador de movimentos --------------------------------------------
FONT_MOVES = ("Verdana", 18, "bold")  # texto do contador
BACKGROUND_COLOR_MOVES = "#8f7a66"    # fundo do contador
FOREGROUND_COLOR_MOVES = "#f9f6f2"    # cor do texto do contador
MOVES_PADDING = 6                     # espaço vertical interno do contador

# --- Teclas ------------------------------------------------------------
KEY_QUIT = "Escape"   # encerra o jogo
KEY_BACK = "b"        # desfaz a última jogada

# Movimento com as setas.
KEY_UP = "Up"
KEY_DOWN = "Down"
KEY_LEFT = "Left"
KEY_RIGHT = "Right"

# Movimento alternativo com W, A, S, D.
KEY_UP_ALT1 = "w"
KEY_DOWN_ALT1 = "s"
KEY_LEFT_ALT1 = "a"
KEY_RIGHT_ALT1 = "d"

# Movimento alternativo com I, J, K, L.
KEY_UP_ALT2 = "i"
KEY_DOWN_ALT2 = "k"
KEY_LEFT_ALT2 = "j"
KEY_RIGHT_ALT2 = "l"