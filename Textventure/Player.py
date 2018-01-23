import ui_util


class Player:

    def __init__(self, game_display, room, inv = []):

        self.room = room
        self.inv = inv
        self.game_display = game_display

    def command(self, c):
        c = c.split(' ')
        if c[0] == 'USE':
            obj = c[1]
            use = c[2]
            target = c[3]
            for i in self.inv:
                if obj == i.name.upper() and use in i.usages.keys():
                    i.use(use, target)
                    break
        elif c[0] == 'TELL':
            npc_n = c[1]
            d = ' '.join(c[2:])
            for npc in self.room.npcs:
                if npc_n == npc.name.upper() and d.upper() in npc.dialogs.keys():
                    npc.dialog(d)
                    break

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