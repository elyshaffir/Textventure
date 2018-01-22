def commands(cmd, player):
    if cmd in global_commands.keys():
        global_commands[cmd](player)
        print player.room.id


# movement
def left_c(player):
    player.room = player.room.left


def right_c(player):
    player.room = player.room.right


def down_c(player):
    player.room = player.room.down


def up_c(player):
    player.room = player.room.up

global_commands = {"LEFT": left_c, "RIGHT": right_c, "DOWN": down_c, "UP": up_c}
keywords = ['USE', 'TELL', 'PICK']