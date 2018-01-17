class Player:

    def __init__(self, room, inv = []):

        self.room = room
        self.inv = inv

    def command(self, c):
        c = c.split(' ')
        if c[0] == 'USE':
            obj = c[1]
            use = c[2]
            target = c[3]
            for i in self.inv:
                if obj == i.name.upper() and use in i.usages.keys():
                    i.use(use, target)
