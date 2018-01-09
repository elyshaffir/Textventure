import pygame, time


def prompt(game_display, text, x = 10, y = 10, color = (0, 0, 0), font = pygame.font.SysFont('Comic Sans MS', 30), delay = .3):

    for i in range(len(text)):
        text_surface = font.render(text[:i + 1], False, color)
        text_surface.get_rect().center = (x, y)
        game_display.blit(text_surface, text_surface.get_rect())
        time.sleep(delay)
        pygame.display.update()
