import pygame


class Cell:
    rows = cols = 9

    def __init__(self, row, col, width, height, val):
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.val = val
        self.selected = False
        self.mutable = (val == 0)
        self.valid = (val != 0)

    def draw(self, window):
        font = pygame.font.SysFont("Arial", 36)
        space = self.width / 9
        x = self.col * space
        y = self.row * space

        # Print Cell value
        font.set_bold(not self.mutable)
        if not(self.val == 0):
            text = font.render(str(self.val), 1, (0, 0, 0))
        else:
            text = font.render(' ', 1, (0, 0, 0))
        window.blit(text, (x + (space/2 - text.get_width()/2),
                           y + (space/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(window, (255, 0, 0), (x, y, space, space), 3)

    # Sets the value of the cell
    def set_val(self, val):
        self.val = val
