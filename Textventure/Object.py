import random
import ui_util


class Object:
    def __init__(self,
                 name,
                 id_n=random.randrange(1024),
                 info='',
                 usages={},
                 image=None):

        self.name = name
        self.id = id_n
        self.info = info
        self.usages = usages  # Dict of usages
        self.image = image

    def use(self, use, target):
        if use in self.usages:
            self.usages[use](target)  # Later will be file with all common usages (all take optional parameter target)

    def pick_event(self, game_display):
        if self.image is not None:
            ui_util.display_image(self.image)
        ui_util.prompt_info(self.info)
