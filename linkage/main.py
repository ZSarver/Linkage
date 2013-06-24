import pygame
from pygame.locals import *

def singleton(cls):
    """singleton decorator retrieved from
    http://wiki.python.org/moin/PythonDecoratorLibrary#Singleton."""
    instance = cls()
    instance.__call__ = lambda: instance
    return instance

@singleton
class Game:
    """The Game class is the uberclass that manages game state. It's
    where all the "global" variables go. There should only be one
    instance of the game state, and hence the singleton decorator.

    Note that since Game is a singleton, any instance of game points
    to the same object in memory. The practical consequence of this is
    that all of our helper functions don't need to be passed a game
    object; they can declare their own, and be guaranteed to be
    working with the right data.

    However, for this trick to work, __init__ needs to be an empty
    method (so that when a "new" instance is created, our data is not
    overwritten,) and our actually init function needs to be something
    else."""
    def add_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

class Player:
    """The Player class is the data structure for housing all the data
    pertaining to players themselves: score, territory, joystick id,
    etc."""
    def __init__(self, joyid):
        self.joyid = joyid
        self.score = 0
        self.territory = None #we don't yet have a territory data
        #structure

def main():
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    if not pygame.joystick.get_init():
        pygame.joystick.init()
    gamepads = [pygame.joystick.Joystick(x) for x in
        range(pygame.joystick.get_count())]

    player1 = Player(gamepade[0].get_id())
    if pygame.joystick.get_count() > 1:
        player2 = Player(gamepads[1].get_id())
    else:
        player2 = Player(None)

    game = Game()
    game.add_players(player1, player2)

    #main loop
    while True:
        #process events
        dispatch_events(pygame.event.get())
        #get input
        #perform game logic
        #output graphics

def dispatch_event(events):
    for event in events:
        #gamepad event
        if event.type == JOYAXISMOTION or event.type == JOYBALLMOTION or event.type == JOYBUTTONDOWN or event.type == JOYBUTTONUP or event.type == JOYHATMOTION:
            handle_joystick_event(event)
    
def handle_joystick_event(event):
    game = Game() #grab the game object
    if event.joy == game.player1.joyid:
        if event.type == JOYAXISMOTION:
            print "blah"
    if event.joy == game.player2.joyid:
        if event.type == JOYAXISMOTION:
            print "blah"
