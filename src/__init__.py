import math
import copy

def main():
    init_board = [
        [0, 0, 0, 0, 0, 2, 1, 0, 0],
        [0, 0, 4, 0, 0, 8, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 9, 0, 0],
        [6, 0, 2, 0, 0, 3, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 6, 0, 0, 3, 0, 1],
        [0, 0, 3, 0, 0, 5, 0, 8, 0],
        [0, 0, 8, 2, 0, 0, 5, 0, 0],
        [0, 0, 9, 7, 0, 0, 0, 0, 0]
    ]

    print("Solving board:")
    print_board(init_board)

    stack = [init_board]

    while len(stack) > 0:
        board = stack.pop()
        slot = get_empty_slot(board)

        if slot is None:
            print("Solved!")
            print_board(board)
            return

        for guess in range(1, 10):
            if is_valid_in_slot(board, slot, guess):
                stack.append(update_board(board, slot, guess))


def get_empty_slot(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return Slot(row, col)

    return None


def is_valid_in_slot(board, slot, guess):
    return is_valid_in_row(board, guess, slot.row) \
        and is_valid_in_column(board, guess, slot.col) \
        and is_valid_in_square(board, slot, guess)


def is_valid_in_row(board, guess, row):
    for col in range(9):
        if board[row][col] == guess:
            return False
    return True


def is_valid_in_column(board, guess, col):
    for row in range(9):
        if board[row][col] == guess:
            return False
    return True


def is_valid_in_square(board, slot, guess):
    square_x = math.floor(slot.row / 3)
    square_y = math.floor(slot.col / 3)

    for row in range(square_x * 3, (square_x + 1) * 3):
        for col in range(square_y * 3, (square_y + 1) * 3):
            if board[row][col] == guess:
                return False

    return True


def update_board(board, slot, guess):
    new_board = copy.deepcopy(board)
    new_board[slot.row][slot.col] = guess
    return new_board


def print_row_line():
    to_print = "-"
    for i in range(9):
        to_print += "--"
    print(to_print)


def print_board(board):
    print_row_line()

    for row in board:
        row_string = "|"
        for cell in row:
            if cell == 0:
                row_string += " |"
            else:
                row_string += f"{cell}|"

        print(row_string)
        print_row_line()


class Slot:
    def __init__(self, row, col):
        self.row = row
        self.col = col
