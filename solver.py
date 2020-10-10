import pygame

bo = [
    [0, 4, 0, 0, 0, 6, 0, 0, 7],
    [1, 0, 0, 0, 0, 2, 4, 6, 9],
    [0, 0, 0, 0, 0, 1, 0, 5, 0],
    [0, 7, 9, 6, 0, 3, 2, 8, 0],
    [2, 8, 0, 4, 0, 0, 0, 0, 0],
    [0, 6, 0, 2, 0, 8, 9, 1, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [8, 1, 4, 3, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 0, 0]
]

# Solves a given Sudoku board using backtracking
# Needs to be a grid in order to be solved with visualizer


def solve(board, window, time):
    for y in range(board.rows):
        for x in range(board.cols):
            if board.cells[x][y].val == 0:
                board.select(x, y)
                for n in range(1, 10):
                    board.place(n)
                    redraw_window_while_solving(window, board, time)
                    pygame.display.update()
                    if is_valid(board.state, y, x, n):
                        #board[x][y] = n

                        # Recursively solve the rest of the board
                        if solve(board, window, time):
                            return True

                        # If incorrect, replace this number and backtrack
                        #board[x][y] = 0
                        board.select(x, y)
                        board.place(0)
                        redraw_window_while_solving(window, board, time)
                        pygame.display.update()
                    else:
                        board.place(0)
                        board.draw(window)
                        pygame.display.update()
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
            if board[x_cell + i][y_cell + j] == n and (x_cell + i != x and y_cell + j != y):
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

# Extra redraw_window so that the solver can redraw the window itself
# Alternatively could move solver methods into game file but I wanted
# to keep them separated


def redraw_window_while_solving(window, board, time):
    window.fill((255, 255, 255))

    # Solver button
    solve_button = pygame.Rect(5, 550, 100, 40)
    pygame.draw.rect(window, (250, 60, 60), solve_button)
    font = pygame.font.SysFont("Arial", 40)
    text = font.render("Solve", 1, (0, 0, 0))
    window.blit(text, (14, 546))

    # Time
    text = font.render("Time: " + time, 1, (0, 0, 0))
    window.blit(text, (540 - 220, 546))

    board.draw(window)
