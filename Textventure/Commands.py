import ui_util
import globals_vars

def commands(cmd, player):
    if cmd in global_commands.keys():
        try:
            global_commands[cmd](player)
            print player.room.id
        except AttributeError:
            ui_util.prompt_info('Can\'t do that.')


# movement
def left_c(player):
    if player.room.left is not None:
        player.room = player.room.left
        globals_vars.current_displaying_info = ''
        globals_vars.current_displaying_image = None
    else:
        raise AttributeError


def right_c(player):
    if player.room.right is not None:
        player.room = player.room.right
        globals_vars.current_displaying_info = ''
        globals_vars.current_displaying_image = None
    else:
        raise AttributeError


def down_c(player):
    if player.room.down is not None:
        player.room = player.room.down
        globals_vars.current_displaying_info = ''
        globals_vars.current_displaying_image = None
    else:
        raise AttributeError


def up_c(player):
    if player.room.up is not None:
        player.room = player.room.up
        globals_vars.current_displaying_info = ''
        globals_vars.current_displaying_image = None
    else:
        raise AttributeError


global_commands = {"LEFT": left_c, "RIGHT": right_c, "DOWN": down_c, "UP": up_c}
keywords = ['USE', 'TELL', 'PICK', 'DROP']