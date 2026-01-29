"""Simple chess game for two players, inspired by Al Sweigart's: 
https://automatetheboringstuff.com/3e/chapter7.html#calibre_link-1572
Slightly modified in my own way.
"""

import sys
import subprocess
import copy

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

BOARD = """
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

def print_chessboard(game_state: dict) -> None:
    """Print the state of the game.
    
    :param game_state (dict): Dictionary with inhabited fields."""
    subprocess.run('clear') # https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module
    squares = []
    is_white_sq = True

    for r, lbl_row in enumerate(LABEL_NUM):
        for c, lbl_col in enumerate(LABEL_CHR):
            coords = lbl_col + lbl_row
            # Starts with black filed 'a8' so (0 + 0) % 2 must evaluet True
            is_white_sq = lambda: BLACK_SQ if (r + c) % 2 == 0 else WHITE_SQ

            if coords in game_state:
                squares.append(game_state[coords])
            else:
                squares.append(is_white_sq())

    print(BOARD.format(*squares))


def move(current_board: dict[str, str], current_pos: str, new_pos: str) -> dict[str, str]:
    """Set new position for a piece. 

    :param current_board (dict): Current game state
    :param current_pos (str): The position of the piece to be changed
    :param new_pos (str): New position of the piece"""

    new_board = copy.copy(current_board)

    new_board[new_pos] = new_board[current_pos]
    del new_board[current_pos]

    return new_board


def main_game(game_pieces):
    while True:
        print_chessboard(game_pieces)
        l = input()
        game_pieces = move(game_pieces, l[0], l[1])

if __name__ == '__main__':
    main_game(STARTING_PIECES)
    