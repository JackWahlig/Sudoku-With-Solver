import pygame
import time
import solver
from cell import Cell
from grid import Grid

pygame.font.init()


def main():
    # Window and game setup
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku with Solver")
    board = Grid(9, 9, 540, 540)

    start_time = time.time()
    key = None
    running = True

    # Game Loop
    while running:
        running_time = round(time.time() - start_time)

        # Observe Actions
        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                running = False

            # Keystrokes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if not (board.selected == None):
                    if event.key == pygame.K_LEFT:
                        if board.selected[0] > 0:
                            board.select(
                                board.selected[0] - 1, board.selected[1])
                            key = None
                    if event.key == pygame.K_UP:
                        if board.selected[1] > 0:
                            board.select(
                                board.selected[0], board.selected[1] - 1)
                            key = None
                    if event.key == pygame.K_RIGHT:
                        if board.selected[0] < 8:
                            board.select(
                                board.selected[0] + 1, board.selected[1])
                            key = None
                    if event.key == pygame.K_DOWN:
                        if board.selected[1] < 8:
                            board.select(
                                board.selected[0], board.selected[1] + 1)
                            key = None

            # Clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                solve_button = pygame.Rect(5, 550, 100, 40)
                position = pygame.mouse.get_pos()
                click_position = board.get_click_pos(position)
                # Solve if solve button is pressed
                if solve_button.collidepoint(position):
                    solver.solve(board, window, formatted_time(running_time))
                # Moved to valid space if clicked on game board
                elif click_position:
                    board.select(click_position[0], click_position[1])
                    key = None

        if board.selected and key != None and board.is_selected_mutable():
            board.place(key)
            key = None
            # Check if done
            if board.is_complete():
                print("Complete! Congrats!")
                running = False

        redraw_window(window, board, running_time)
        pygame.display.update()


def redraw_window(window, board, time):
    window.fill((255, 255, 255))

    # Solver button
    solve_button = pygame.Rect(5, 550, 100, 40)
    pygame.draw.rect(window, (250, 60, 60), solve_button)
    font = pygame.font.SysFont("Arial", 40)
    text = font.render("Solve", 1, (0, 0, 0))
    window.blit(text, (14, 546))

    # Time
    text = font.render("Time: " + formatted_time(time), 1, (0, 0, 0))
    window.blit(text, (540 - 220, 546))

    board.draw(window)


def formatted_time(seconds):
    secs = seconds % 60
    if secs > 9:
        secs_str = str(secs)
    else:
        secs_str = "0" + str(secs)
    mins = seconds // 60
    if mins > 9:
        mins_str = str(mins)
    else:
        mins_str = "0" + str(mins)
    hours = mins // 60
    if hours > 9:
        hours_str = str(hours)
    else:
        hours_str = "0" + str(hours)

    time = hours_str + ":" + mins_str + ":" + secs_str
    return time


main()
