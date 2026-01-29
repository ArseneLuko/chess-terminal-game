"""Simple chess game for two players, inspired by Al Sweigart's: 
https://automatetheboringstuff.com/3e/chapter7.html#calibre_link-1572
Slightly modified in my own way.
"""

import sys, copy

STARTING_PIECES = {
    'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
    'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR',

    'a7': 'bP', 'b7': 'bP', 'c7': 'bP', 'd7': 'bP',
    'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',

    'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
    'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP',

    'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ',
    'e1': 'wK', 'f1': 'wB', 'g1': 'wN', 'h1': 'wR'
    }

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____           
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""

WHITE_SQ = '  '
BLACK_SQ = '||'

LABEL_CHR = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
LABEL_NUM = ['8', '7', '6', '5', '4', '3', '2', '1']

def print_chessboard(board):
    squares = []
    is_white_sq = True
    for num_row, lbl_row in enumerate(LABEL_NUM):
        for num_col, lbl_col in enumerate(LABEL_CHR):
            coords = lbl_col + lbl_row
            is_white_sq = lambda: BLACK_SQ if (num_row + num_col) % 2 == 0 else WHITE_SQ
            if coords in STARTING_PIECES:
                squares.append(STARTING_PIECES[coords])
            else:
                squares.append(is_white_sq())
            # print(f'coord: {coords} / {is_white_sq()}') # DEBUG

    # print(3 * '\n') # DEBUG
    print(BOARD_TEMPLATE.format(*squares))

print_chessboard(BOARD_TEMPLATE)
