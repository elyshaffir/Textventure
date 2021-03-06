import pygame, pickle, os, shutil
import Object
import ui_util


class Player:
    def __init__(self, game_display, room, inv=[]):

        self.room = room
        self.inv = inv
        self.game_display = game_display

    def ret_obj(self, obj_string):
        for obj in self.inv:
            if obj.name.upper() == obj_string.upper():
                return obj

        return None

    def objects_n(self):
        o_n = []
        for obj in self.inv:
            o_n.append(obj.name.upper())
        return o_n

    def all_object_usages(self):
        a_o_u = []
        for obj in self.inv:
            for key in obj.usages.keys():
                a_o_u.append(str(key))
        return a_o_u

    def command(self, c):
        limit = len(c)
        for i in range(limit):
            cmd = c[i].upper()
            if cmd == 'USE':
                try:
                    i += 1
                    if i < limit:
                        obj = c[i].upper()
                        if obj not in self.objects_n():
                            ui_util.prompt_info(obj + '? You dont have such object')
                            break
                    else:
                        ui_util.prompt_info("Use what?")
                        break

                    i += 1
                    if i < limit:
                        use = c[i].upper()
                        if use not in self.ret_obj(obj).usages.keys():
                            ui_util.prompt_info('You can\'t ' + use + ' with this ' + obj)
                            break
                    else:
                        ui_util.prompt_info("What for?")
                        break

                    i += 1
                    if i < limit:
                        target = c[i].upper()
                    else:
                        ui_util.prompt_info("And do that to whom?")
                        break

                    ob = self.ret_obj(obj)
                    ob.use(use, target)
                    break
                except IndexError:
                    ui_util.prompt_info('Can\'t do that.')

            elif cmd == 'TELL':
                try:
                    i += 1
                    if i < limit:
                        npc_n = c[i].upper()
                        if npc_n not in self.room.npcs_n():
                            ui_util.prompt_info(npc_n + '? There is no such person in this room')
                            break
                    else:
                        ui_util.prompt_info('Tell who?')
                        break

                    i += 1
                    if i < limit:
                        d = c[i].upper()
                        if d not in self.room.ret_npc(npc_n).dialogs.keys():
                            ui_util.prompt_info(npc_n + ' has nothing to say about that')
                            break
                    else:
                        ui_util.prompt_info('What do you wanna tell ' +  npc_n + '?')
                        break

                    npc = self.room.ret_npc(npc_n)
                    npc.dialog(d)
                    break
                except IndexError:
                    ui_util.prompt_info('Can\'t do that.')

            elif cmd == 'PICK':
                i += 1
                if i < limit:
                    obj_n = c[i].upper()
                    if obj_n not in self.room.objects_n():

                        if obj_n in self.objects_n():
                            ui_util.prompt_info('You already own that.')
                            return

                        ui_util.prompt_info(obj_n + '? Not in this room!')
                        break
                else:
                    ui_util.prompt_info("Pick what?")
                    break

                obj = self.room.ret_obj(obj_n)
                self.inv.append(obj)
                self.room.objects.remove(obj)
                obj.pick_event()
                return

            elif cmd == 'DROP':
                try:
                    i += 1

                    if (i < limit):
                        obj_n = c[i].upper()
                        if obj_n in self.objects_n():
                            obj = self.ret_obj(obj_n)
                            self.inv.remove(obj)
                            self.room.objects.append(obj)
                            ui_util.prompt_info('the ' + obj_n + ' has been dropped.')
                            break
                        else:
                            ui_util.prompt_info('You don\'t have any ' + obj_n)
                            break
                    else:
                        ui_util.prompt_info('What would you like to drop, kind sir?')
                        break

                except IndexError:
                    ui_util.prompt_info('Can\'t do that.')

            elif cmd == 'SAVE':
                i += 1
                if i < limit:
                    ui_util.prompt_info('You saved the game. The save is called: ' + c[i].upper())
                    self.save(c[i].upper())
                else:
                    ui_util.prompt_info('How you wanna call your save?')
                    break

            elif cmd == 'LOAD':
                i += 1
                if i < limit:
                    ui_util.prompt_info('You have loaded the save: ' + c[i].upper())
                    self.load(c[i].upper())
                else:
                    ui_util.prompt_info('Load what?')
                    break

    def save(self, filename):
        path = 'saves/' + filename + '/inv'
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            shutil.rmtree(path)
            os.makedirs(path)
        path += '/'
        for obj in self.inv:
            obj1 = Object.Object(name=obj.name,
                                 info=obj.info,
                                 usages=obj.usages,
                                 image=obj.image_n,
                                 w=obj.w,
                                 h=obj.h)
            obj1.image = None
            self.save_by_name(path + obj1.name, obj1)

        path = 'saves/' + filename + '/rms'
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            shutil.rmtree(path)
            os.makedirs(path)
        path += '/'
        self.room.save(path, True)

    def load(self, filename):
        path = 'saves/' + filename + '/inv/'
        self.inv = []
        for obj in os.listdir(path):
            obj1 = self.load_by_name(path + obj)
            obj1.image = pygame.image.load(obj1.image_n)
            obj1.image = pygame.transform.scale(self.image, (obj1.w, obj1.h))
            self.inv.append(obj1)

        try:
            self.room = self.load_by_name('saves/' + filename + '/rms/gene.pkl')
        except Exception:
            pass
        path = 'saves/' + filename + '/rms/'
        self.room.load(path, self.game_display, True)

    @staticmethod
    def save_by_name(name, v):
        with open(name + '.pkl', 'wb') as f:
            pickle.dump(v, f)

    @staticmethod  # If a function in a class doesn't use 'self', its static and its best to say it.
    def load_by_name(name):
        with open(name, 'rb') as f:
            data = pickle.load(f)
        return data
