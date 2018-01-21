import pygame

pygame.init()

import Room, ChatBox, NPC, Player, Object
from globals import *

import ui_util


game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

joe = NPC.NPC(game_display, 'Joe', {'FUCK YOU': 'Nah fuck you!'})

genesis = Room.Room(npcs=[joe])

player = Player.Player(genesis)

cb = ChatBox.ChatBox(player = player)
font = pygame.font.SysFont('Comic Sans MS', 30)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    game_display.fill(BACKGROUND)
    ui_util.frame(game_display, 10, 450, 780, 140, color = FOREGROUND)
    ui_util.frame(game_display, 10, 10, 780, 430, color = FOREGROUND)
    cb.printer(game_display, font)
    pygame.display.update()
