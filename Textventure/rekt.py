import pygame, numpy
import scripts, colors, beam

class Rekt:

    def __init__(self,
                 game_display,
                 position,
                 color,
                 def_w = 10,
                 def_h = 10,
                 w = None,
                 h = None,
                 shrink = False,
                 shrink_w = None,
                 shrink_h = None,
                 spd_e = 0,
                 shooting = False,
                 shoot_to = [],
                 b_type = 0):

        self.def_w = def_w
        self.def_h = def_h
        self.w = w
        if self.w == None:
            self.w = def_w
        self.h = h
        if self.h == None:
            self.h = def_h
        self.position = position
        self.game_display = game_display
        self.color = color
        self.x_spd = 0
        self.y_spd = 0
        self.trail_cells = [[-100, -100],
                            [-100, -100],
                            [-100, -100],
                            [-100, -100],
                            [-100, -100],
                            [position[0], position[1]]]
        self.shrink = shrink
        self.shrink_w = shrink_w
        self.shrink_h = shrink_h
        if self.shrink_w == None:
            self.shrink_w = self.w / 5
        else:
            self.shrink_w = shrink_w
        if self.shrink_h == None:
            self.shrink_h = self.h / 5
        else:
            self.shrink_h = shrink_h

        self.spd_e = spd_e
        self.shooting = shooting
        self.shoot_to = shoot_to
        self.b_type = b_type

    def draw(self):
        pygame.draw.rect(self.game_display,
                         self.color,
                         [self.position[0], self.position[1], self.w, self.h])

    # basic movement
    def controller(self, spd, col_list, beam_list, dead_beams):
        # expext no movement
        move_x = 0
        move_y = 0.5

        # Expext no shrink
        self.shrink = False

        # Spd boost
        spd += self.spd_e

        # Shooting
        self.shooting = False

        # find movement direction
        k = pygame.key.get_pressed()
        if k[pygame.K_RIGHT] or k[pygame.K_d]:
            move_x += 1
        if k[pygame.K_LEFT] or k[pygame.K_a]:
            move_x -= 1

        if k[pygame.K_UP] or k[pygame.K_w]:
            move_y -= 1
        if k[pygame.K_DOWN] or k[pygame.K_s]:
            move_y += 1

        if k[pygame.K_LSHIFT] or k[pygame.K_RSHIFT]:
            if not self.shrink:
                pass # Move to prevent glitching through blocks

            self.shrink = True

        # if k[pygame.K_SPACE] and not self.shrink:
        #     self.shooting = True
        self.shoot_to = self.shooter(k)

        # apply movement direction
        self.x_spd = move_x * spd
        self.y_spd = move_y * spd

        # shrinker
        if self.shrink:
            self.w = self.shrink_w
            self.h = self.shrink_h
        elif not scripts.collision_all(Rekt(self.game_display, self.position, self.color, w = self.def_w, h = self.def_h), col_list + dead_beams):
            self.w = self.def_w
            self.h = self.def_h

    # M0v3m3nt & C0ll1s10n
    def move(self, col_list):
        # x collision
        if scripts.collision_all(self, col_list, self.x_spd) or scripts.collision_out_of_bound(self, x_add = self.x_spd):
            while not (scripts.collision_all(self, col_list, numpy.sign(self.x_spd)) or scripts.collision_out_of_bound(self, x_add = numpy.sign(self.x_spd))):
                self.position[0] += numpy.sign(self.x_spd)
        else:
        # x movement
            self.position[0] += self.x_spd

        # y collision
        if scripts.collision_all(self, col_list, 0, self.y_spd) or scripts.collision_out_of_bound(self, y_add = self.y_spd):
            while not (scripts.collision_all(self, col_list, 0, numpy.sign(self.y_spd)) or scripts.collision_out_of_bound(self, y_add = numpy.sign(self.y_spd))):
                self.position[1] += numpy.sign(self.y_spd)
        else:
        # y movement
            self.position[1] += self.y_spd

    def trail(self):
            self.trail_cells[-1] = [self.position[0], self.position[1]]
            for i in range(len(self.trail_cells) - 1):
                self.trail_cells[i] = self.trail_cells[i + 1]

            trail_color = 255
            # cur_color = colors.brighten(self.color, 180)
            cur_color = self.color
            cur_colors = []
            for cell in self.trail_cells:
                cur_colors.append(cur_color)
                cur_color = colors.brighten(cur_color, 0.25)

            color_index = len(self.trail_cells) - 1
            for cell in self.trail_cells:
                pygame.draw.rect(self.game_display,
                                 cur_colors[color_index],
                                 [cell[0], cell[1], self.w, self.h])
                color_index -= 1

    def shoot(self, beam_list, way, b_type = 0):
        b = beam.Beam(self.game_display, way, self.position, b_type = b_type)
        beam_list.append(b)

    def shooter(self, k):
        way = []
        if k[pygame.K_i]:
            self.shooting = True
            way.append(0)

        elif k[pygame.K_k]:
            self.shooting = True
            way.append(1)

        if k[pygame.K_j]:
            self.shooting = True
            way.append(3)

        elif k[pygame.K_l]:
            self.shooting = True
            way.append(2)

        if k[pygame.K_1]:
            self.b_type = 0
        if k[pygame.K_2]:
            self.b_type = 1
        if k[pygame.K_3]:
            self.b_type = 2
        if k[pygame.K_4]:
            self.b_type = 3
        if k[pygame.K_5]:
            self.b_type = 4
        if k[pygame.K_6]:
            self.b_type = 5

        return way
