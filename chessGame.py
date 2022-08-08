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
                self.board[col+row] = '  '
        
    def draw(self):
        # prints current state of the game/board
        print('    a    b    c    d    e    f    g    h')
        print(' +----+----+----+----+----+----+----+----+')       
        for row in '87654321':
            print(f'{row}|',end='')
            for col in 'abcdefgh':
                print(f' {self.board[col+row]} |',end='')
            print(f'{row}\n +----+----+----+----+----+----+----+----+')
        print('    a    b    c    d    e    f    g    h')

    def set (self, pos, val):
        # sets new value for a given position (x, R, P, ...)
        self.board[pos] = val

class Player ():
    def __init__(self, board, name, color ) -> None:
        # initializes new player; super to AI class
        self.name = name
        self.color = color
        self.make_pieces(board)

    def make_pieces(self, board):
        # sets pieces 
        if self.color == 'white':
            board.set('a1', 'wR')
            board.set('h1', 'wR')
            board.set('b1', 'wN')
            board.set('g1', 'wN')
            board.set('c1', 'wB')
            board.set('f1', 'wB')
            board.set('d1', 'wQ')
            board.set('e1', 'wK')
            for col in 'abcdefgh':
                board.set(col+'2','wP')
        else:
            board.set('a8', 'bR')
            board.set('h8', 'bR')
            board.set('b8', 'bN')
            board.set('g8', 'bN')
            board.set('c8', 'bB')
            board.set('f8', 'bB')
            board.set('d8', 'bQ')
            board.set('e8', 'bK')
            for col in 'abcdefgh':
                board.set(col+'7','bP')

    def get_player_move (self):
        pass


class AI (Player):
    def __init__(self, board, name, color) -> None:
        super().__init__(board, name, color)



def main ():
    print('Welcome to the chess game!')
    #color_choice = input('Please choose your color (W/w for white; B/b for black):\n')
    #match = 
    game = Game()
    print(game.board)
    user = Player(game, 'User', 'white')
    computer = AI(game, 'Computer Player', 'black')
    game.draw()


main()