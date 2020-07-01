bo = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Solves a given Sudoku board using backtracking


def solve(board):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                for n in range(1, 10):
                    if is_valid(board, x, y, n):
                        board[x][y] = n

                        # Recursively solve the rest of the board
                        if solve(board):
                            return True

                        # If incorrect, replace this number and backtrack
                        board[x][y] = 0
                return False
    return True

# Tests to see if value n is a valid number at location (x, y)


def is_valid(board, x, y, n):
    if n > 9 or n < 1:
        return False
    # Check same row and column
    for i in range(0, len(board)):
        if (board[x][i] == n and i != y) or (board[i][y] == n and i != x):
            return False
    # Check same 3x3 cell
    x_cell = (x // 3) * 3
    y_cell = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[x_cell + i][y_cell + j] == n and (x_cell != x and y_cell != y):
                return False

    return True

# Prints out 9x9 sudoku grid. For testing prior to GUI implementation


def print_board(board):

    for i in range(len(board)):
        if i != 0 and i % 3 == 0:
            print()

        for j in range(len(board[0])):
            if j != 0 and j % 3 == 0:
                print(" ", end="")

            if j != 8:
                print(str(board[i][j]) + " ", end="")
            else:
                print(str(board[i][j]))
