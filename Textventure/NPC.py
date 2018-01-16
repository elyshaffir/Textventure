class NPC:

    def __init__(self, dialogs, acts):
        self.dialogs = dialogs  # Dict of functions
        self.acts = acts  # Dict of functions

    def dialog(self, d):
        self.dialogs[d]()

    def act(self, a):
        self.acts[a]()
