#!/cygdrive/c/Program Files/Python38/python

# Testing file to try things out
# Using the Pygame official docs:
# https://www.pygame.org/docs/

# Example file showing a basic pygame "game loop"
import pygame
from pygame import Color

# sizes
width = 1280
height = 720
cell_width = 16
cell_height = 16

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
running = True

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
            col = (mouse_pos[1] - (mouse_pos[1] % 16)) // 16
            row = (mouse_pos[0] - (mouse_pos[0] % 16)) // 16

            print(row, col)
            print(mouse_pos)

            cells[row // 16][col // 16] = not cells[row // 16][col // 16]
            cell = pygame.Rect(row, col, cell_width, cell_height)



    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_color)
    cornercell = pygame.draw.rect(screen, colors[1], corner)
    for row in range(rows):
        for col in range(cols):
            cell = pygame.Rect(row * 16, col * 16, cell_width, cell_height)
            if cells[row // cell_width][col // cell_width]:
                pygame.draw.rect(screen, colors[1], cell)
            else:
                pygame.draw.rect(screen, colors[0], cell)
        

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()