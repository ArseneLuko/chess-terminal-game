"""Simple chess game for two players, inspired by Al Sweigart's: 
https://automatetheboringstuff.com/3e/chapter7.html#calibre_link-1572
Slightly modified in my own way.
"""

import sys
import subprocess
import copy
from constants import STARTING_PIECES, BOARD, WHITE_SQ, BLACK_SQ, LABEL_CHR, LABEL_NUM

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


def game_move(current_board: dict[str, str], current_pos: str, new_pos: str) -> dict[str, str]:
    """Set new position for a piece. 

    :param current_board (dict): Current game state
    :param current_pos (str): The position of the piece to be changed
    :param new_pos (str): New position of the piece"""

    new_board = copy.copy(current_board)

    new_board[new_pos] = new_board[current_pos]
    del new_board[current_pos]

    return new_board


def main_game(game_pieces):
    white_turns = True # white player starts
    msg = ''

    while True:
        print_chessboard(game_pieces)
        print(msg)
        print(f'Na tahu je {'bílý (w)' if white_turns else 'černý (b)'} hráč')
        move = input('> ').split()
        game_pieces = game_move(game_pieces, move[0], move[1])
        white_turns = not white_turns

if __name__ == '__main__':
    main_game(STARTING_PIECES)
    