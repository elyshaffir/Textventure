import pygame
import Commands
from globals import *


class ChatBox:

    def __init__(self, player):

        self.player = player

        self.string = ''
        self.letter = ''
        self.prv_ltr = ''
        self.og_text = []
        self.write_place = 0

        # certain key hold timers
        self.ers_timer = 0
        self.wl_timer = 0
        self.wr_timer = 0

        self.type_timer = 0
        self.type_ltr = '_'

        # last string
        self.last_index = 0
        self.last_string = []

    def write_with_color(self, text, color, game_display, font):
        for count in range(len(text), 0, -1):
            string = ''
            # builds sentece from end to color over it
            for word in text[:count]:
                string += word
            text_surface = font.render(string, False, color[count - 1])
            game_display.blit(text_surface, (15, 530))

    def erase(self):
        place = -self.write_place
        if place == 0:
            self.string = self.string[:-1]
        else:
            self.string = self.string[:place - 1] + self.string[place:]

    def w_left(self):
        if self.write_place < len(self.string):
            self.write_place += 1
            self.type_timer = 1000

    def w_right(self):
        if self.write_place > 0:
            self.write_place -= 1
            self.type_timer = 1000

    def hold_function(self, letter, func, timer, delay = 325, speed = 30):
        # function
        if self.letter == letter:
            # first press
            if timer == 0:
                func()
            # after holding
            if timer > delay and timer % speed == 0:
                func()

            # hold timer
            timer += 1
            self.letter = ''
        else:
            # reset hold timer
            timer = 0
        return timer

    def write(self, place, letter):
        if place == 0:
            self.string += letter
        else:
            self.string = self.string[:place] + letter + self.string[place:]

    def letter_exc(self, a, b):
        if self.letter == a:
            self.letter = b

    def inputer(self):
        # letter reset
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
            if k[pygame.K_RIGHT]:
                self.letter = '--right--'
            if k[pygame.K_LEFT]:
                self.letter = '--left--'
            if k[pygame.K_UP]:
                self.letter = '--up--'
            if k[pygame.K_DOWN]:
                self.letter = '--down--'

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
        self.ers_timer = self.hold_function('--backspace--', self.erase, self.ers_timer)

        # moving the write place left
        self.wl_timer = self.hold_function('--left--', self.w_left, self.wl_timer)

        # moving the write place right
        self.wr_timer = self.hold_function('--right--', self.w_right, self.wr_timer)

        # single press key functions
        if self.letter != self.prv_ltr:

            # previus letter: checks fir single press
            self.prv_ltr = self.letter

            # previus string
            if self.letter == '--up--':
                if self.last_index < len(self.last_string):
                    self.write_place = 0
                    self.last_index += 1
                    self.string = self.last_string[-self.last_index]

                self.letter = ''

            # next string
            if self.letter == '--down--':
                if self.last_index > 0:
                    self.last_index -= 1
                    self.write_place = 0
                    if self.last_index == 0:
                        self.string = ''
                    else:
                        self.string = self.last_string[-self.last_index]

                self.letter = ''

            # submitting
            if self.letter == '--enter--':
                self.write_place = 0

                # storing prvs strings
                self.last_string.append(self.string)
                self.last_index = 0
                # clearing string
                self.string = ''
                self.letter = ''

                # doing commands
                self.player.command(self.og_text)
                Commands.commands(self.og_text, self.player)
                self.player.room.command(self.og_text)
                print self.og_text

            # adding to string
            if (self.letter != ''):
                if k[pygame.K_LSHIFT] or k[pygame.K_RSHIFT]:
                    # turn / to ?
                    self.letter_exc('/', '?')
                    # turn 1 to !
                    self.letter_exc('1', '!')

                    # upper case letters
                    self.letter = self.letter.upper()

                self.write(-self.write_place, self.letter)

    def printer(self, game_display, font):
        place = len(self.string) - self.write_place

        self.inputer()
        if self.type_timer == 500:
            self.type_ltr = ' '

        if self.type_timer == 1000:
            self.type_ltr = '_'
            self.type_timer = 0

        self.type_timer += 1

        stringer = self.string[:place] + self.type_ltr
        text_surface = font.render(stringer, False, FOREGROUND)
        game_display.blit(text_surface, (15, 530))

        split_string = self.string.split(' ')
        text = []
        og_text = []
        color = []
        i = 0
        while i < len(split_string):
            # original word backup
            og_text.append(split_string[i])

            # remove unwanted space
            while i + 1 < len(split_string) and split_string[i + 1] == '':
                split_string[i] += ' '
                del split_string[i + 1]

            if og_text[i].upper() in Commands.global_commands.keys():
                color.append(COMMAND)
            elif og_text[i].upper() in Commands.keywords:
                color.append(KEYWORD)
            elif og_text[i].upper() in self.player.room.objects_n():
                color.append(OBJ)
            elif (og_text[i].upper() in self.player.room.all_object_usages()
                or og_text[i].upper() in self.player.all_object_usages()):
                color.append(USAGE_C)
            elif og_text[i].upper() in self.player.objects_n():
                color[i] = INV_C
            elif og_text[i].upper() in self.player.room.npcs_n():
                color.append(NPC_C)
            elif og_text[i].upper() in self.player.room.all_npc_acts():
                color.append(ACT_C)
            elif og_text[i].upper() in COLOURS.keys():
                color.append(COLOURS[og_text[i].upper()])
            else:
                color.append(OTHER)

            if i > 0 and color[i] == (OTHER) and color[i - 1] == (OTHER):
                og_text[i - 1] += ' ' + og_text[i]
                split_string[i - 1] += ' ' + split_string[i]
                del split_string[i]
                del og_text[i]
                del color[i]
                i -= 1
                if og_text[i].upper() in Commands.global_commands.keys():
                    color[i] = COMMAND
                elif og_text[i].upper() in Commands.keywords:
                    color[i] = KEYWORD
                elif og_text[i].upper() in self.player.room.objects_n():
                    color[i] = OBJ
                elif og_text[i].upper() in self.player.objects_n():
                    color[i] = INV_C
                elif og_text[i].upper() in self.player.room.npcs_n():
                    color[i] = NPC_C
                else:
                    color[i] = OTHER

                text[i] = split_string[i] + ' '

            else:
                text.append(split_string[i] + ' ')
            i += 1
        self.og_text = og_text
        self.write_with_color(text, color, game_display, font)
