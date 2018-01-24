import random
import ui_util

class Room:

    def __init__(self,
                left = None, right = None, up = None, down = None,
                id_n = random.randrange(1024),
                info = '',
                commands = {},
                npcs = [],
                objects = []):

        self.id = id_n

        # Rooms around + Rooms around around.
        self.left = left
        self.right = right
        self.up = up
        self.down = down

        if left is not None:
            self.left.right = self

        if right is not None:
            self.right.left = self

        if up is not None:
            self.up.down = self

        if down is not None:
            self.down.up = self

        self.info = info
        self.commands = commands  # Dictionary
        self.npcs = npcs
        self.objects = objects
        self.objects_n = []
        for obj in objects:
            self.objects_n.append(obj.name.upper())

        self.npcs_n = []
        for npc in npcs:
            self.npcs_n.append(npc.name.upper())

    def command(self, c):
        if c in self.commands.keys():
            self.commands[c]()
        else:
            c1 = c.split(' ')
            for npc in self.npcs:
                try:
                    if c1[-1] == npc.name.upper() and c1[:-1] in npc.acts:
                        npc.act(c1[:-1])
                except TypeError:
                    ui_util.prompt_info('Invalid command.')
