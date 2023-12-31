#!/cygdrive/c/Program Files/Python38/python

# Implementation of John Conway's Game of Life using Pygame
# https://playgameoflife.com/
# Using the Pygame official docs:
# https://www.pygame.org/docs/

# Example file showing a basic pygame "game loop"
import pygame
from pygame import Color

# sizes
width = 1280
height = 720
cell_width = 4
cell_height = 4

rows = width // cell_width
cols = height // cell_height



# with width/height of 16 there can be a grid of 80 x 45 cells
# this grid will be a 2D array of T/F for alive/dead, indices determine location
cells = [[False for j in range(rows)] for i in range(cols)]
print(len(cells))
print(len(cells[0]))

pygame.init()
screen = pygame.display.set_mode((width, height))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
clock = pygame.time.Clock()
running = True # Overall game is running
generating = False # Cells are being drawn and removed

# color creation
background_color = Color(199, 229, 237)
dead_color = Color(117, 84, 89)
alive_color = Color(41, 230, 179)
colors = [dead_color, alive_color]

# cell creation
cell = pygame.Rect(width / 2, height / 2, cell_width, cell_height)
corner = pygame.Rect(0, 0, cell_width, cell_height)


# grid_lines = pygame.draw.rect(screen, alive_color, cell)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # determine which cell the mouse is in, and toggle the life status!
            col = (mouse_pos[1] - (mouse_pos[1] % cell_width)) // cell_width
            row = (mouse_pos[0] - (mouse_pos[0] % cell_width)) // cell_width

            print(row, col)
            print(mouse_pos)

            cells[row // cell_width][col // cell_width] = not cells[row // cell_width][col // cell_width]
            cell = pygame.Rect(row, col, cell_width, cell_height)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # start and stop generating by using the space bar
                generating = not generating

    if generating:
        # (src: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Rules)
        # check all cells for the following conditions:
        # Any live cell with fewer than two live neighbors dies by underpopulation.
        # Any live cell with 2 or three live neighbors lives on to the next generation.
        # Any live cell with > 3 live neighbours dies, as if by overpopulation.
        # Any dead cell with 3 live neighbours becomes alive as if by reproduction.
        num_adjacent = 0
        print(len(cells))
        print(len(cells[0]))
        print(rows)
        print(cols)
        for col in range(cols):
            for row in range(rows):
                # count its live neighbors :)
                # print(row, col)
                num_adjacent = 0
                # check for live cells laterally (col to left and right!)
                if col >= 1:
                    if cells[col - 1][row]:
                        num_adjacent += 1
                if col < cols - 1:
                    if cells[col + 1][row]:
                        num_adjacent += 1
                # and now vertically (row to left and right) and corners
                if row >= 1:
                    if cells[col][row - 1]:
                        num_adjacent += 1
                    if col >= 1:
                        if cells[col - 1][row - 1]:
                            num_adjacent += 1
                    if col < cols - 2:
                        if cells[col + 1][row - 1]:
                            num_adjacent += 1
                if row < rows - 2:
                    if cells[col][row + 1]:
                        num_adjacent += 1
                    if col >= 1:
                        if cells[col - 1][row + 1]:
                            num_adjacent += 1
                    if col < cols - 2:
                        if cells[col + 1][row + 1]:
                            num_adjacent += 1
                # Any dead cell with 3 live neighbours -> alive as if by reproduction.
                if not cells[col][row]:
                    if num_adjacent == 3:
                        cells[col][row] = True
                else: # cell is alive
                    # Any live cell with fewer than two live neighbors dies.
                    if num_adjacent < 2:
                        cells[col][row] = False
                    # Any live cell with 2 or three live neighbors survives.
                    elif num_adjacent == 2 or num_adjacent == 3:
                        cells[col][row] = True
                    # Any live cell with > 3 live neighbours dies.
                    elif num_adjacent > 3:
                        cells[col][row] = False



    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_color)
    cornercell = pygame.draw.rect(screen, colors[1], corner)
    for row in range(rows):
        for col in range(cols):
            cell = pygame.Rect(row * cell_width, col * cell_width, cell_width, cell_height)
            if cells[row // cell_width][col // cell_width]:
                pygame.draw.rect(screen, colors[1], cell)
            else:
                pygame.draw.rect(screen, colors[0], cell)



    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

# # (src: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Rules)
# # check all cells for the following conditions:
# # Any live cell with fewer than two live neighbors dies by underpopulation.
# # Any live cell with 2 or three live neighbors lives on to the next generation.
# # Any live cell with > 3 live neighbours dies, as if by overpopulation.
# # Any dead cell with 3 live neighbours becomes alive as if by reproduction.
# num_adjacent = 0

# for row in range(rows):
#     for col in range(cols):
#         # count its live neighbors :)
#         num_adjacent = 0
#         # check for live cells laterally (col to left and right!)
#         if col >= 1:
#             if cells[row][col - 1]:
#                 num_adjacent += 1
#         if col < cols - 1:
#             if cells[row][col + 1]:
#                 num_adjacent += 1
#         # and now vertically (row to left and right) and corners
#         if row >= 1:
#             if cells[row - 1][col]:
#                 num_adjacent += 1
#             if col >= 1:
#                 if cells[row - 1][col - 1]:
#                     num_adjacent += 1
#             if col < cols - 1:
#                 if cells[row - 1][col + 1]:
#                     num_adjacent += 1
#         if row < rows - 1:
#             if cells[row + 1][col]:
#                 num_adjacent += 1
#             if col >= 1:
#                 if cells[row + 1][col - 1]:
#                     num_adjacent += 1
#             if col < cols - 1:
#                 if cells[row + 1][col + 1]:
#                     num_adjacent += 1
#         # Any dead cell with 3 live neighbours -> alive as if by reproduction.
#         if not cells[row][col]:
#             if num_adjacent == 3:
#                 cells[row][col] = True
#         else: # cell is alive
#             # Any live cell with fewer than two live neighbors dies.
#             if num_adjacent < 2:
#                 cells[row][col] = False
#             # Any live cell with 2 or three live neighbors survives.
#             elif num_adjacent == 2 or num_adjacent == 3:
#                 cells[row][col] = True
#             # Any live cell with > 3 live neighbours dies.
#             elif num_adjacent > 3:
#                 cells[row][col] = False
