# actual game. should use the text output (simple, rudimentary) 


from chessMoves import evaluate
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

    def get_poss_moves(self, c):
        b = evaluate(c)
        for i in b.items():
            if i[1] == 'x' and self.board[i[0]] == '  ':
                self.board[i[0]] = 'x '

    def clear(self):
        for i in self.board.items():
            if i[1] == 'x ':
                self.board[i[0]] = '  '
            

class Player ():
    def __init__(self, board, name, color ) -> None:
        # initializes new player; super to AI class
        self.name = name
        self.color = color
        self.make_pieces(board)
        self.player_choice = ''

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

    def get_player_move (self, board):
        while True:
            self.player_choice = input('please enter the piece you want to move (by tile eg a1, f3,...)\n')
            if board.board[self.player_choice][0] == self.color[0]:
                print('that is a valid choice!')
                return board.board[self.player_choice][1:2] + self.player_choice
                break
            else:
                print('not a valid choice!')
                continue



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
    while True:
        game.clear()
        game.draw()
        choice = user.get_player_move(game)
        game.get_poss_moves(choice)


main()