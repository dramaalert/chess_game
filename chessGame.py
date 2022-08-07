# actual game. should use the text output (simple, rudimentary) 


import chessMoves
import re


class Game ():
    def __init__(self) -> None:
        # initializes dictionary 'board'
        self.board = {}
        # populates the board with blanks
        for row in '12345678':
            for col in 'abcdefgh':
                self.board[col+row] = ' '
        
    def __str__(self) -> str:
        print('   a   b   c   d   e   f   g   h')
        print(' +---+---+---+---+---+---+---+---+')       
        for row in '87654321':
            print(f'{row}|',end='')
            for col in 'abcdefgh':
                print(f' {self.board[col+row]} |',end='')
            print('\n +---+---+---+---+---+---+---+---+')
        print('   a   b   c   d   e   f   g   h')

class Player ():
    def __init__(self, name, color ) -> None:
        self.name = name
        self.color = color

    def make_pieces(self):
        if 

    def get_player_move (self):
        pass



def main ():
    print('Welcome to the chess game!')
    color_choice = input('Please choose your color (W/w for white; B/b for black):\n')
    match = 
    game = Game()
    print(game)
    user = Player('User', input('Please choose your color (W/w for white; B/b for black):\n'))


main()