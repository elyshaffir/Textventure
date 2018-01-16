class NPC:

    def __init__(self, name, dialogs, acts):

        self.name = name
        self.dialogs = dialogs  # Dict of functions
        self.acts = acts  # Dict of functions

    def dialog(self, d):
        if d in self.dialogs.keys():
            self.dialogs[d]()  # Later print

    def act(self, a):
        if a in self.acts.keys():
            self.acts[a]()
