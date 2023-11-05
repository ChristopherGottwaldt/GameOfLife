#!/usr/bin/env python3

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 540))
clock = pygame.time.Clock()
running = True

# render loop
while running:
    #poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen to overwrite all contents
    screen.fill("purple")

    # render game

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limit fps to tick rate
    clock.tick(60)

# while loop has ended
pygame.quit()
