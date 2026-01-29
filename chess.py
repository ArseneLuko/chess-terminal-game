"""Simple chess game for two players, inspired by Al Sweigart's: 
https://automatetheboringstuff.com/3e/chapter7.html#calibre_link-1572
Slightly modified in my own way.
"""

import sys
import subprocess
import copy
from constants import STARTING_PIECES, BOARD, WHITE_SQ, BLACK_SQ, LABEL_CHR, LABEL_NUM

class Game:
    def __init__(self) -> None:
        self.game_state = copy.copy(STARTING_PIECES)
        self.white_turns = True # white player starts
        self.check_move_msg = None
        self.message = lambda: print(self.check_move_msg) if self.check_move_msg else print()
  
    def run(self):
        while True:
            self.print_chessboard()
            self.message()
            print(f'Na tahu je {'bílý (w)' if self.white_turns else 'černý (b)'} hráč')

            move = input('> ').split()

            self.check_move_msg = self.check_move(move[0], move[1])

            if self.check_move_msg:
                continue
            
            self.game_move(move[0], move[1])  

            self.white_turns = not self.white_turns
      

    def print_chessboard(self) -> None:
        """Print the current state of the game."""
        subprocess.run('clear') # https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module
        squares = []
        is_white_sq = True

        for r, lbl_row in enumerate(LABEL_NUM):
            for c, lbl_col in enumerate(LABEL_CHR):
                coords = lbl_col + lbl_row
                # Starts with black filed 'a8' so (0 + 0) % 2 must evaluet True
                is_white_sq = lambda: BLACK_SQ if (r + c) % 2 == 0 else WHITE_SQ

                if coords in self.game_state:
                    squares.append(self.game_state[coords])
                else:
                    squares.append(is_white_sq())

        print(BOARD.format(*squares))

    def game_move(self, current_pos: str, new_pos: str) -> None:
        """Set new position for a piece. 

        :param current_pos (str): The position of the piece to be changed
        :param new_pos (str): New position of the piece"""

        self.game_state[new_pos] = self.game_state[current_pos]
        del self.game_state[current_pos]

    def check_move(self, current_pos: str, new_pos: str):
        if current_pos not in self.game_state:
            return "Zvolené pole není obsazeno žádnou figurou, vyberte pole s figurou."

if __name__ == '__main__':
    game = Game()
    game.run()
    