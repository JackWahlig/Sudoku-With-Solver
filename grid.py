import pygame
from cell import Cell
import solver


class Grid:
    board = [
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

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.cells = [[Cell(i, j, width, height, self.board[i][j])
                       for i in range(rows)] for j in range(cols)]
        self.selected = None
        self.state = None
        self.update_state()

    def draw(self, window):
        # Grid line
        space = self.width / 9
        for i in range(self.rows + 1):
            if i != 0 and i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(window, (0, 0, 0), (0, i * space),
                             (self.width, i * space), thickness)
            pygame.draw.line(window, (0, 0, 0), (i * space, 0),
                             (i * space, self.height), thickness)

        # Cells
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(window)

    # Updates values currently in the grid
    def update_state(self):
        self.state = [[self.cells[i][j].val for i in range(
            self.rows)] for j in range(self.cols)]

    # Checks to see if the game is done
    def is_complete(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.cells[i][j].valid:
                    return False
        return True

    # Selects the cell clicked on
    def select(self, row, col):
        # Reset other selections
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].selected = False
        # Select new cell
        self.cells[row][col].selected = True
        self.selected = [row, col]

    # Gets the row and col of a cell based on where it's clicked
    def get_click_pos(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            space = self.width / 9
            x = pos[0] // space
            y = pos[1] // space
            return [int(x), int(y)]
        else:
            return None

    # Checks if the selected cell is mutable
    def is_selected_mutable(self):
        return self.cells[self.selected[0]][self.selected[1]].mutable

    # Inserts an entered value into a cell
    def place(self, val):
        row, col = self.selected
        self.cells[row][col].set_val(val)

        # Check if placement is valid to keep track for completion
        if solver.is_valid(self.state, col, row, val):
            print(True)
            self.cells[row][col].valid = True
        else:
            print(False)
            self.cells[row][col].valid = False

        self.update_state()

    # Deletes every value in a cell

    def clear(self):
        row, col = self.selected
        self.cells[row][col].set_val(0)
        self.update_state()
