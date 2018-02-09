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

        self.all_npc_a = []
        for npc in npcs:
            for key in npc.acts.keys():
                self.all_npc_a.append(str(key))

    def ret_obj(self, obj_string):
        for obj in self.objects:
            if obj.name.upper() == obj_string.upper():
                return obj

        return None

    def command(self, cmd):
        # for every command in the string
        for i in range(len(cmd)):
            # curnnet command that is checking
            c1 = cmd[i].upper()
            # room commands
            if c1 in self.commands.keys():
                self.commands[c1]()
            elif i > 0:
                # the act
                c2 = cmd[i-1].upper()
                # npc acts
                for npc in self.npcs:
                    try:
                        if (c1 == npc.name.upper() and c2 in npc.acts):
                            npc.act(c2)
                    except TypeError:
                        ui_util.prompt_info('Invalid command.')
