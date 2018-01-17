import random


class Object:

    def __init__(self,
                name,
                id_n = random.randrange(1024),
                info = '',
                usages = {}):

        self.name = name
        self.id = id_n
        self.info = info
        self.usages = usages  # Dict of usages

    def use(self, use, target):
        if use in self.usages:
            self.usages[use](target)  # Later will be file with all common usages (all take optional parameter target)