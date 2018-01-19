import pygame, time
from globals import *


def prompt(game_display, text, x = 10, y = 10, color = FOREGROUND, font = pygame.font.SysFont('Comic Sans MS', 30), delay = .3):

    for i in range(len(text)):
        text_surface = font.render(text[:i + 1], False, color)
        text_surface.get_rect().center = (x, y)
        game_display.blit(text_surface, text_surface.get_rect())
        time.sleep(delay)
        pygame.display.update()


def frame(game_display, x, y, w, h, color = FOREGROUND, s = 3):
    pygame.draw.rect(game_display, color, [x, y, w, h], s)
