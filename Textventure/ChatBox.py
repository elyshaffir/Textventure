import pygame

class ChatBox:

    def __init__(self):
        self.string = ''
        self.letter = ''
        self.prv_ltr = ''

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
                self.letter = '-'
            if k[pygame.K_SPACE]:
                self.letter = ' '

        if (self.letter != self.prv_ltr):
            # previus letter
            self.prv_ltr = self.letter

            # erasing
            if self.letter == '-':
                self.string = self.string[:-1]
                self.letter = ''
                print(self.string)

            # adding to string
            if (self.letter != ''):
                if k[pygame.K_LSHIFT]:
                    self.string += self.letter.upper()
                else:
                    self.string += self.letter

                print(self.string)
