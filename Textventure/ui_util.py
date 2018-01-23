import pygame, time
import globals_vars
from globals import *


def prompt(game_display, text, x = 15, y = 15, color = FOREGROUND, font = pygame.font.SysFont('Comic Sans MS', 30), delay = .08):

    for i in range(len(text)):
        text_surface = font.render(text[:i + 1], False, color)
        game_display.blit(text_surface, (x, y))
        time.sleep(delay)
        pygame.display.update()

    globals_vars.current_displaying_info = ''
    globals_vars.current_displaying_image = None
    globals_vars.current_displaying_text = text


def frame(game_display, x, y, w, h, color = FOREGROUND, s = 3):
    pygame.draw.rect(game_display, color, [x, y, w, h], s)


def display_image(image):
    globals_vars.current_displaying_text = ''
    globals_vars.current_displaying_image = image


def prompt_info(info):
    globals_vars.current_displaying_text = ''
    globals_vars.current_displaying_info = info