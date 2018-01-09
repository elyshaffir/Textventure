import random


class Object:

    def __init__(self,
                id_n = random.randrange(1024),
                info = '',
                commands = []):

        self.id = id_n
        self.info = info
        self.commands = commands        
