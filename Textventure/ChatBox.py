import pygame
import Commands

class ChatBox:

    def __init__(self, player):

        self.player = player

        self.string = ''
        self.letter = ''
        self.prv_ltr = ''
        self.ltr_cnt = 0

    def letter_exc(self, a, b):
        if self.letter == a:
            self.letter = b

    def inputer(self):
        self.letter = ''
        k = pygame.key.get_pressed()

        # a-z & others input
        if True:
            # a-z
            if k[pygame.K_a]:
                self.letter = 'a'
            if k[pygame.K_b]:
                self.letter = 'b'
            if k[pygame.K_c]:
                self.letter = 'c'
            if k[pygame.K_d]:
                self.letter = 'd'
            if k[pygame.K_e]:
                self.letter = 'e'
            if k[pygame.K_f]:
                self.letter = 'f'
            if k[pygame.K_g]:
                self.letter = 'g'
            if k[pygame.K_h]:
                self.letter = 'h'
            if k[pygame.K_i]:
                self.letter = 'i'
            if k[pygame.K_j]:
                self.letter = 'j'
            if k[pygame.K_k]:
                self.letter = 'k'
            if k[pygame.K_l]:
                self.letter = 'l'
            if k[pygame.K_m]:
                self.letter = 'm'
            if k[pygame.K_n]:
                self.letter = 'n'
            if k[pygame.K_o]:
                self.letter = 'o'
            if k[pygame.K_p]:
                self.letter = 'p'
            if k[pygame.K_q]:
                self.letter = 'q'
            if k[pygame.K_r]:
                self.letter = 'r'
            if k[pygame.K_s]:
                self.letter = 's'
            if k[pygame.K_t]:
                self.letter = 't'
            if k[pygame.K_u]:
                self.letter = 'u'
            if k[pygame.K_v]:
                self.letter = 'v'
            if k[pygame.K_w]:
                self.letter = 'w'
            if k[pygame.K_x]:
                self.letter = 'x'
            if k[pygame.K_y]:
                self.letter = 'y'
            if k[pygame.K_z]:
                self.letter = 'z'

            # other stuff
            if k[pygame.K_BACKSPACE]:
                self.letter = '--backspace--'
            if k[pygame.K_SPACE]:
                self.letter = ' '
            if k[pygame.K_SLASH]:
                self.letter = '/'
            if k[pygame.K_PERIOD]:
                self.letter = '.'

            # numbers
            if k[pygame.K_0]:
                self.letter = '0'
            if k[pygame.K_1]:
                self.letter = '1'
            if k[pygame.K_2]:
                self.letter = '2'
            if k[pygame.K_3]:
                self.letter = '3'
            if k[pygame.K_4]:
                self.letter = '4'
            if k[pygame.K_5]:
                self.letter = '5'
            if k[pygame.K_6]:
                self.letter = '6'
            if k[pygame.K_7]:
                self.letter = '7'
            if k[pygame.K_8]:
                self.letter = '8'
            if k[pygame.K_9]:
                self.letter = '9'

            # commands
            if k[pygame.K_RETURN]:
                self.letter = '--enter--'

        # erasing
        if self.letter == '--backspace--':
            if self.ltr_cnt == 0 or (self.ltr_cnt > 600 and self.ltr_cnt % 50 == 0):
                self.string = self.string[:-1]
            self.ltr_cnt += 1
            self.letter = ''
        else:
            self.ltr_cnt = 0

        # wait for key release
        if self.letter != self.prv_ltr:

            # previus letter
            self.prv_ltr = self.letter

            # submitting
            if self.letter == '--enter--':
                Commands.commands(self.string.upper(), self.player)
                self.player.room.command(self.string.upper())
                self.player.command(self.string.upper())
                self.string = ''
                self.letter = ''


            # adding to string
            if (self.letter != ''):
                if k[pygame.K_LSHIFT] or k[pygame.K_RSHIFT]:
                    # turn / to ?
                    self.letter_exc('/', '?')
                    # turn 1 to !
                    self.letter_exc('1', '!')

                    self.string += self.letter.upper()
                else:
                    self.string += self.letter

    def printer(self, game_display, font):
        self.inputer()
        text_surface = font.render(self.string + '|', False, (0, 0, 0))
        text_surface.get_rect().center = (100, 100)
        game_display.blit(text_surface, text_surface.get_rect())
