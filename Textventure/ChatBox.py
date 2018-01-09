import pygame
import ui_util


class ChatBox:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.text = ''
        self.max_len = 20
