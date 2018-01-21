import pygame, time
from globals import *


def prompt(game_display, text, x = 15, y = 15, color = FOREGROUND, font = pygame.font.SysFont('Comic Sans MS', 30), delay = .3):

    for i in range(len(text)):
        text_surface = font.render(text[:i + 1], False, color)
        game_display.blit(text_surface, (x, y))
        time.sleep(delay)
        pygame.display.update()


def frame(game_display, x, y, w, h, color = FOREGROUND, s = 3):
    pygame.draw.rect(game_display, color, [x, y, w, h], s)
