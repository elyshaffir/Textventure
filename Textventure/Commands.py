def commands(cmd, player):
    global_commands[cmd](player)


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
