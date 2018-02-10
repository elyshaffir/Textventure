import pygame, random, pickle, os
import Object, NPC
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

    def save(self, path, gene = False):
        if str(self.id) + '.pkl' not in os.listdir(path):
            if gene:
                path1 = path + '/objsgene'
                path2 = path + '/npcsgene'
            else:
                path1 = path + '/objs' + str(self.id)
                path2 = path + '/npcs' + str(self.id)
            if not os.path.exists(path1):
                os.makedirs(path1)
            if not os.path.exists(path2):
                os.makedirs(path2)

            path1 += '/'
            for obj in self.objects:
                obj1 = Object.Object(name=obj.name,
                                     info=obj.info,
                                     usages=obj.usages,
                                     image=obj.image_n,
                                     w=obj.w,
                                     h=obj.h)
                obj1.image = None
                self.save_by_name(path1 + obj1.name, obj1)

            path2 += '/'
            for npc in self.npcs:
                npc1 = NPC.NPC(game_display=None, name=npc.name, dialogs=npc.dialogs, acts=npc.acts)
                self.save_by_name(path2 + npc1.name, npc1)
            try:
                if gene:
                    self.save_by_name(path + 'gene', self)
                else:
                    self.save_by_name(path + str(self.id), self)
            except Exception:
                pass

        if self.left is not None:
            if str(self.left.id) + '.pkl' not in os.listdir(path):
                self.left.save(path)
        if self.right is not None:
            if str(self.right.id) + '.pkl' not in os.listdir(path):
                self.right.save(path)
        if self.up is not None:
            if str(self.up.id) + '.pkl' not in os.listdir(path):
                self.up.save(path)
        if self.down is not None:
            if str(self.down.id) + '.pkl' not in os.listdir(path):
                self.down.save(path)

    def load(self, path, game_display, gene = False):
        if gene:
            room_name = 'gene'
        else:
            room_name = str(self.id)

        objs = path + 'objs' + room_name + '/'
        self.objects = []
        for obj in os.listdir(objs):
            obj1 = self.load_by_name(objs + obj)
            obj1.image = pygame.image.load(obj1.image_n)
            obj1.image = pygame.transform.scale(obj1.image, (obj1.w, obj1.h))

            self.objects.append(obj1)
        self.objects_n = []
        for obj in self.objects:
            self.objects_n.append(obj.name.upper())

        npcs = path + 'npcs' + room_name + '/'
        self.npcs = []

        for npc in os.listdir(npcs):
            npc1 = self.load_by_name(npcs + npc)
            npc1.game_display = game_display
            self.npcs.append(npc1)
            self.npcs_n = []
        for npc in self.npcs:
            self.npcs_n.append(npc.name.upper())

        if self.left is not None:
            if str(self.left.id) + '.pkl' not in os.listdir(path):
                self.left.load(path)
        if self.right is not None:
            if str(self.right.id) + '.pkl' not in os.listdir(path):
                self.right.load(path)
        if self.up is not None:
            if str(self.up.id) + '.pkl' not in os.listdir(path):
                self.up.load(path)
        if self.down is not None:
            if str(self.down.id) + '.pkl' not in os.listdir(path):
                self.down.load(path)

    @staticmethod
    def save_by_name(name, v):
        with open(name + '.pkl', 'wb') as f:
            pickle.dump(v, f)

    @staticmethod  # If a function in a class doesn't use 'self', its static and its best to say it.
    def load_by_name(name):
        with open(name, 'rb') as f:
            data = pickle.load(f)
        return data