import ui_util

class NPC:

    def __init__(self, game_display, name, dialogs = {}, acts = {}):

        self.game_display = game_display
        self.name = name
        self.dialogs = dialogs  # Dict of responses
        self.acts = acts  # Dict of functions

    def dialog(self, d):
        if d in self.dialogs.keys():
            ui_util.prompt(self.game_display, self.dialogs[d])

    def act(self, a):
        if a in self.acts.keys():
            self.acts[a]()
