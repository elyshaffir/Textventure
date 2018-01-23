import pygame

pygame.init()

import Room, ChatBox, NPC, Player, Object
from globals import *
import globals_vars

import ui_util


game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

joe = NPC.NPC(game_display, 'Joe', {'FUCK YOU': 'Nah fuck you!'})
chicken_leg = Object.Object('Chicken',
                            info = 'Its a fucking chicken leg.',
                            image = pygame.image.load('imgs/pulke.png'),
                            w = 780, h = 370)

genesis = Room.Room(npcs=[joe], objects=[chicken_leg])

player = Player.Player(game_display, genesis)

cb = ChatBox.ChatBox(player = player)
font = pygame.font.SysFont('Comic Sans MS', 30)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    game_display.fill(BACKGROUND)

    ui_util.frame(game_display, 10, 10, 780, 60, color=FOREGROUND)
    ui_util.frame(game_display, 10, 80, 780, 60, color=FOREGROUND)
    ui_util.frame(game_display, 10, 150, 780, 370, color=FOREGROUND)
    ui_util.frame(game_display, 10, 530, 780, 60, color = FOREGROUND)

    cb.printer(game_display, font)

    text_surface = font.render(globals_vars.current_displaying_text, False, FOREGROUND)
    game_display.blit(text_surface, (15, 15))

    text_surface = font.render(globals_vars.current_displaying_info, False, FOREGROUND)
    game_display.blit(text_surface, (15, 85))

    if globals_vars.current_displaying_image is not None:
        game_display.blit(globals_vars.current_displaying_image, (15, 155))

    pygame.display.update()
