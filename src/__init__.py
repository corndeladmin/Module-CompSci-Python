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
            if is_valid_slot(board, slot, guess):
                if is_valid_slot(board, slot, guess):
                    stack.append(update_board(board, slot, guess))


def get_empty_slot(board):
    raise Exception("Fill Me In!")
    return Slot(0, 0)


def is_valid_slot(board, slot, guess):
    return is_valid_in_row(board, guess, slot.row) \
        and is_valid_in_column(board, guess, slot.col) \
        and is_valid_in_square(board, slot, guess)


def is_valid_in_row(board, guess, row):
    raise Exception("Fill Me In!")
    return True


def is_valid_in_column(board, guess, col):
    raise Exception("Fill Me In!")
    return True


def is_valid_in_square(board, slot, guess):
    raise Exception("Fill Me In!")
    return True


def update_board(board, slot, guess):
    raise Exception("Fill Me In!")


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
