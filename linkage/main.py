import pygame
from pygame.locals import *

from gameelements import *

def singleton(cls):
    """singleton decorator retrieved from
    http://wiki.python.org/moin/PythonDecoratorLibrary#Singleton."""
    instance = cls()
    instance.__call__ = lambda: instance
    return instance

def dispatch_events(events):
    for event in events:
        #gamepad event
        if event.type == JOYAXISMOTION or event.type == JOYBALLMOTION or event.type == JOYBUTTONDOWN or event.type == JOYBUTTONUP or event.type == JOYHATMOTION:
            handle_joystick_event(event)
        if event.type == QUIT:
            exit()
    
def handle_joystick_event(event):
    game = Game() #grab the game object
    if event.joy == game.player1.joyid:
        if event.type == JOYAXISMOTION:
            print "blah"
    if event.joy == game.player2.joyid:
        if event.type == JOYAXISMOTION:
            print "blah"

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
    def new(self):
        self.board = Gameboard()
    def add_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

class Player:
    """The Player class is the data structure for housing all the data
    pertaining to players themselves: score, territory, joystick id,
    etc."""
    mouse = 0
    other = 1
    def __init__(self, joyid):
        self.joyid = joyid
        self.score = 0
        self.territory = None #we don't yet have a territory data
        #structure
        #we need a convenient way of locking the cursor to the
        #relevant parts of the UI if the player is using a gamepad
        #or keyboard. Here's a first attempt
        self.cursor = Cursor()
        

class Cursor:
    """The Cursor class keeps track of where the player is pointing."""
    def __init__(self):
        self._screenpos = Rect(320,240,0,0)
        self._boardpos = [0,0]
        self._uilock = False #whether the cursor is currently locked to
        #the ui. False by default
        self._dirty = True

    def draw(self):
        if uilock:
            #erase mouse cursor
        if not uilock:
            #draw mouse cursor 
        #hilight correct cell on gameboard
        self.clean()
    
    def clean(self):
        self._dirty = False

    @property
    def screenpos(self):
        return self._screenpos

    @screenpos.setter
    def screenpos(self, value):
        self._dirty = True
        self._screenpos = value

    @property
    def boardpos(self):
        return self._boardpos
    
    @boardpos.setter
    def boardpos(self, value):
        self._dirty = True
        self._boardpos = value

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
    game.new()
    game.add_players(player1, player2)

    #main loop
    while True:
        #process events
        dispatch_events(pygame.event.get())
        pygame.event.pump()
        #get input
        #perform game logic
        #output graphics

if __name__ == "__main__":
    main()
