import pygame
import Room, ChatBox, NPC, Player

pygame.init()


def test():
    pass

game_display = pygame.display.set_mode((800, 600))

genesis = Room.Room()
r1 = Room.Room(commands={'TEST': test}, left = genesis)

player = Player.Player(genesis)

cb = ChatBox.ChatBox(player = player)
font = pygame.font.SysFont('Comic Sans MS', 30)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    game_display.fill((255, 255, 255))
    cb.printer(game_display, font)
    pygame.display.update()
