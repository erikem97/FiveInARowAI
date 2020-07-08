import numpy as np

class BOARD:
    def __init__(self, row_length, column_length):
        self.board = np.zeros(shape=(row_length, column_length))
        self.row_length = row_length
        self.column_length = column_length
        self.number_diagonals = row_length+column_length-1

    def print_board(self):
        print(self.board)

    def add_marker(self, row, column, mark):
        self.board[row, column] = mark

    def check_win(self, mark):
        horizontal = 0

        for row in range(self.row_length):
            for column in range(self.column_length):
                if horizontal == 5:
                    return True
                if self.board[row, column] == mark:
                    horizontal += 1
                else:
                    horizontal = 0
        vertical = 0
        for column in range(self.column_length):
            for row in range(self.row_length):
                if vertical == 5:
                    return True
                if self.board[row, column] == mark:
                    vertical += 1
                else:
                    vertical = 0

        diagonal_check = 0
        diagonal = self.board.diagonal()
        for i in range(len(diagonal)):
            if diagonal[i] == mark:
                diagonal_check += 1
            else:
                diagonal_check = 0
            if diagonal_check == 5:
                return True

        for i in range(round(self.number_diagonals/2)):
            diagonal = self.board.diagonal(-i)
            for i in range(len(diagonal)):
                if diagonal[i] == mark:
                    diagonal_check += 1
                else:
                    diagonal_check = 0
                if diagonal_check == 5:
                    return True
            diagonal = self.board.diagonal(i)
            for i in range(len(diagonal)):
                if diagonal[i] == mark:
                    diagonal_check += 1
                else:
                    diagonal_check = 0
                if diagonal_check == 5:
                    return True

            diagonal_check = 0
            diagonal = np.fliplr(self.board).diagonal()
            for i in range(len(diagonal)):
                if diagonal[i] == mark:
                    diagonal_check += 1
                else:
                    diagonal_check = 0
                if diagonal_check == 5:
                    return True

            for i in range(round(self.number_diagonals / 2)):
                diagonal = np.fliplr(self.board).diagonal()
                for i in range(len(diagonal)):
                    if diagonal[i] == mark:
                        diagonal_check += 1
                    else:
                        diagonal_check = 0
                    if diagonal_check == 5:
                        return True
                diagonal = np.fliplr(self.board).diagonal()
                for i in range(len(diagonal)):
                    if diagonal[i] == mark:
                        diagonal_check += 1
                    else:
                        diagonal_check = 0
                    if diagonal_check == 5:
                        return True




    def check_occupied(self, row, column):
        if self.board[row, column] != 0:
            print("That spot is already occupied")
            return False
        else:
            return True

    def check_size_constraint(self, row, column):
        if self.row_length-1 < row or self.column_length-1 < column:
            print("That is out of bounds!")
            return False
        else:
            return True

    def check_input(self, row, column):
        if self.check_size_constraint(row, column):
            if self.check_occupied(row, column):
                return True

            else:
                return False
        else:
            return False

    def check_draw(self):
        for row in range(self.column_length):
            for column in range(self.row_length):
                if self.board[row, column] == 0:
                    return False


    def check_win_mark(self):
        if self.check_win(1):
            print("Winner is player 1")
            return True
        if self.check_win(2):
            print("Winner is player 2")
            return True
        if self.check_draw() != False:
            print('It is a draw')
            return True


def Game():
    board = BOARD(row_length=15, column_length=15)
    board.print_board()
    while(True):

        row = int(input("Give row value player 1: "))
        column = int(input("Give column value player 1: "))
        while board.check_input(row, column) == False:
            row = int(input("Give row value player 1: "))
            column = int(input("Give column value player 1: "))

        board.add_marker(row, column, 1)
        board.print_board()

        if board.check_win_mark():
            break

        row = int(input("Give row value player 2: "))
        column = int(input("Give column value player 2: "))
        while board.check_input(row, column) == False:
            row = int(input("Give row value player 2: "))
            column = int(input("Give column value player 2: "))


        board.add_marker(row, column, 2)
        board.print_board()

        if board.check_win_mark():
            break

Game()