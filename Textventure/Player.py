import pygame, pickle, os
import Object
import ui_util


class Player:
    def __init__(self, game_display, room, inv=[]):

        self.room = room
        self.inv = inv
        self.game_display = game_display

    def command(self, c):
        c = c.split(' ')
        if c[0] == 'USE':
            try:
                obj = c[1]
                use = c[2]
                target = c[3]
                for i in self.inv:
                    if obj == i.name.upper() and use in i.usages.keys():
                        i.use(use, target)
                        break
            except IndexError:
                ui_util.prompt_info('Can\'t do that.')

        elif c[0] == 'TELL':
            try:
                npc_n = c[1]
                d = ' '.join(c[2:])
                for npc in self.room.npcs:
                    if npc_n == npc.name.upper() and d.upper() in npc.dialogs.keys():
                        npc.dialog(d)
                        break
            except IndexError:
                ui_util.prompt_info('Can\'t do that.')

        elif c[0] == 'PICK':
            obj_n = ' '.join(c[1:])

            for obj in self.room.objects:
                if obj_n == obj.name.upper():
                    self.inv.append(obj)
                    self.room.objects.remove(obj)
                    obj.pick_event()
                    return

            for obj in self.inv:
                if obj_n == obj.name.upper():
                    ui_util.prompt_info('You already own that.')
                    return

            ui_util.prompt_info('No such object.')

        elif c[0] == 'DROP':
            obj_n = ' '.join(c[1:])

            try:
                for i in self.inv:
                    if obj_n == i.name.upper():
                        self.inv.remove(i)
                        self.room.objects.append(i)
                        self.room.objects_n.append(obj_n)
                        ui_util.prompt_info('Item dropped.')
                        break
            except IndexError:
                ui_util.prompt_info('Can\'t do that.')

        elif c[0] == 'SAVE':
            self.save(c[1])

        elif c[0] == 'LOAD':
            self.load(c[1])

    def save(self, filename):
        path = 'saves/' + filename + '/inv'
        if not os.path.exists(path):
            os.makedirs(path)

        path += '/'
        for obj in self.inv:
            obj1 = Object.Object(name=obj.name,
                                 info=obj.info,
                                 usages=obj.usages,
                                 image=obj.image_n)
            obj1.image = None
            self.save_by_name(path + obj1.name, obj1)

    def load(self, filename):
        path = 'saves/' + filename + '/inv/'
        self.inv = []
        for obj in os.listdir(path):
            obj1 = self.load_by_name(path + obj)
            obj1.image = pygame.image.load(obj1.image_n)
            self.inv.append(obj1)

    @staticmethod
    def save_by_name(name, v):
        with open(name + '.pkl', 'wb') as f:
            pickle.dump(v, f)

    @staticmethod  # If a function in a class doesn't use 'self', its static and its best to say it.
    def load_by_name(name):
        with open(name, 'rb') as f:
            data = pickle.load(f)
        return data
