import pygame
from pygame.locals import *

from eventhandling import *
from gameelements import *
from gameboard import *

def main():
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    if not pygame.joystick.get_init():
        pygame.joystick.init()
    gamepads = [pygame.joystick.Joystick(x) for x in
        range(pygame.joystick.get_count())]

    if len(gamepads) > 0:
        player1 = Player(gamepads[0].get_id())
        if pygame.joystick.get_count() > 1:
            player2 = Player(gamepads[1].get_id())
        else:
            player2 = Player(None)
    else:
        player1 = Player(None)
        player2 = Player(None)

    game = Game()
    game.new(screen)
    game.add_players(player1, player2)

    #main loop
    while True:
        #process events
        dispatch_events(pygame.event.get())
        pygame.event.pump()
        #get input
        #perform game logic
        #output graphics
        game.board.draw()
        game.cursor.draw()
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
