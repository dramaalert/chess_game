# assignment: programming assignment 5
# author: Lucais Sanderson
# date: 09 March 2022
# file: chess.py is a program that shows the possible moves of a given chess piece at a spot on the chess board.
# input: The user inputs a sequence of 2 letters and a number. The first letter corresponds to the desired chess piece.
# The second letter corresponds to the column and the number to the row.
# output: An empty chess board is generated and then the user is asked for input. After the code is entered, a new board
# is generated with the chess piece placed at the coordinate and the possible moves are shown.

import re


class Board:
    def __init__(self):
        self.board = {}
        self.empty()

    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col+row] = ' '

    def set(self, pos, label):
        self.board[pos] = label

    def draw(self):
        print('   a   b   c   d   e   f   g   h\n'
              ' +---+---+---+---+---+---+---+---+')
        for row in '87654321':
            print(f'{row}', end='')
            for column in 'abcdefgh':
                print(f'| {self.board[column+row]} ', end='')
            print(f'|{row}\n +---+---+---+---+---+---+---+---+')
        print('   a   b   c   d   e   f   g   h')


class Chess_Piece:
    def __init__(self, board, pos, color='white'):
        self.position = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())
        self.moves(board, pos)

    def get_index(self, pos):
        return 'abcdefgh'.index(pos[0]), '12345678'.index(pos[1])

    def get_name(self):
        pass

    def moves(self, board, pos):
        pass


class Rook (Chess_Piece):
    def get_name(self):
        return 'R'

    def moves(self, board, pos):
        for col in 'abcdefgh':
            if col != pos[0]:
                board.set(col+pos[1], 'x')
        for row in '12345678':
            if row != pos[1]:
                board.set(pos[0]+row, 'x')


class King (Chess_Piece):
    def get_name(self):
        return 'K'

    def moves(self, board, pos):
        global x, y
        poss_moves_tup = [(self.position[0] + 1, self.position[1]), (self.position[0] + 1, self.position[1] + 1),
                          (self.position[0], self.position[1] + 1), (self.position[0]-1, self.position[1]+1),
                          (self.position[0]-1, self.position[1]), (self.position[0]-1, self.position[1]-1),
                          (self.position[0], self.position[1]-1), (self.position[0]+1, self.position[1]-1)]
        for position in poss_moves_tup:
            if 0 <= position[0] <= 7 and 0 <= position[1] <= 7:
                x = 'abcdefgh'[position[0]]
                y = '12345678'[position[1]]
            board.set(x+y, 'x')


class Knight (Chess_Piece):
    def get_name(self):
        return 'N'

    def moves(self, board, pos):
        for key in board.board.keys():  # traverse all squares
            key_index = self.get_index(key)  # convert keys into indexes
            if key_index[0] == self.position[0] + 1 and key_index[1] == self.position[1] + 2:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] + 2 and key_index[1] == self.position[1] + 1:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] + 2 and key_index[1] == self.position[1] - 1:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] + 1 and key_index[1] == self.position[1] - 2:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] - 1 and key_index[1] == self.position[1] - 2:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] - 2 and key_index[1] == self.position[1] - 1:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] - 2 and key_index[1] == self.position[1] + 1:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] - 1 and key_index[1] == self.position[1] + 2:
                board.set(key, 'x')


class Bishop (Chess_Piece):
    def get_name(self):
        return 'B'

    def moves(self, board, pos):
        for key in board.board.keys():  # traverse all squares
            key_index = self.get_index(key)  # convert keys into indexes
            if abs(self.position[0] - key_index[0]) == abs(self.position[1] - key_index[1]):
                if key_index != self.position:
                    board.set(key, 'x')


class Pawn (Chess_Piece):
    def get_name(self):
        return 'P'

    def moves(self, board, pos):
        pass  # your code goes here


class Queen (Chess_Piece):
    def get_name(self):
        return 'Q'

    def moves(self, board, pos):
        for key in board.board.keys():  # traverse all squares
            key_index = self.get_index(key)  # convert keys into indexes
            if abs(self.position[0] - key_index[0]) == abs(self.position[1] - key_index[1]):
                if key_index != self.position:
                    board.set(key, 'x')
        for col in 'abcdefgh':
            if col != pos[0]:
                board.set(col+pos[1], 'x')
        for row in '12345678':
            if row != pos[1]:
                board.set(pos[0]+row, 'x')


x, y = 0, 0


def main():
    if __name__ == '__main__':
        print('Welcome to the Chess Game!')
        board = Board()
        board.draw()
        #print(f'{board.board}')
        while True:
            board.empty()
            choice = input('Enter a chess piece and its position or type X to exit:\n').lower()
            match = re.match(r'[krqpbn][a-h][1-8]', choice)
            try:
                if choice == 'x':
                    print('Goodbye!')
                    break
                elif match.group():
                    if choice[0] == 'r':
                        rook = Rook(board, choice[1:3])
                        board.draw()
                    elif choice[0] == 'q':
                        queen = Queen(board, choice[1:3])
                        board.draw()
                    elif choice[0] == 'k':
                        king = King(board, choice[1:3])
                        board.draw()
                    elif choice[0] == 'b':
                        bishop = Bishop(board, choice[1:3])
                        board.draw()
                    elif choice[0] == 'n':
                        knight = Knight(board, choice[1:3])
                        board.draw()
                else:
                    print('its a no go')
            except AttributeError:
                continue
            except:
                print('error_unknown')
                break


main()
