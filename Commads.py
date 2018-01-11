global_commands = ["LEFT": Left_c, "RIGHT": Right_c, "DOWN": Down_c, "UP": Up_c]

def Commads(cmd):
    global_commands[cmd]()


# movement
def Left_c():
    Player.room = Player.room.left

def Right_c():
    Player.room = Player.room.right

def Down_c():
    Player.room = Player.room.down

def Up_c():
    Player.room = Player.room.up
