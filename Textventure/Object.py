import pygame, random
import ui_util


class Object:
    def __init__(self,
                 name,
                 id_n = random.randrange(1024),
                 info = '',
                 usages = {},
                 image = None,
                 w = 32,
                 h = 32):

        self.name = name
        self.id = id_n
        self.info = info
        self.usages = usages  # Dict of usages
        self.image = image
        if self.image is not None:
            self.image = pygame.transform.scale(self.image, (w, h))

    def use(self, use, target):
        if use in self.usages:
            self.usages[use](target)  # Later will be file with all common usages (all take optional parameter target)

    def pick_event(self):
        if self.image is not None:
            ui_util.display_image(self.image)
        ui_util.prompt_info(self.info)
