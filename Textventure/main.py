import pygame
import Room

pygame.init()

import ui_util

game_display = pygame.display.set_mode((800, 600))
genesis = Room.Room()
r1 = Room.Room(left = genesis)
r2 = Room.Room(left = r1)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ui_util.prompt(game_display, str(genesis.id)  + ': ' + str(r2.left.left.id) + ': ' + str(genesis.right.right.id))
            pygame.quit()
            quit()
    game_display.fill((255, 255, 255))
    pygame.display.update()
