import pygame
from math import sqrt
from gameboard import *
from drawing import safeload

def singleton(cls):
    """singleton decorator retrieved from
    http://wiki.python.org/moin/PythonDecoratorLibrary#Singleton."""
    instance = cls()
    instance.__call__ = lambda: instance
    return instance
    
@singleton
class Game():
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
    def new(self, surface):
        self.board = Gameboard(surface)
        self.cursor = Cursor(surface)
    def add_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

class Player(object):
    """The Player class is the data structure for housing all the data
    pertaining to players themselves: score, territory, joystick id,
    etc."""
    mouse = 0
    other = 1
    def __init__(self, joyid):
        self.joyid = joyid
        self.score = 0
        
class Cursor(object):
    """The Cursor class keeps track of where the player is pointing.
    drawsurface is the surface to which the cursor should draw itself,
    typically the screen."""
    def __init__(self, drawsurface):
        self._screenpos = (320,240)
        self.oldpos = self.screenpos
        self._boardpos = (4,8)
        self.image = safeload("pointeredited.png")
        self.drawsurface = drawsurface

        self.uilock = False #whether the cursor is currently locked to
        #the ui. False by default
        self._dirty = True

    def draw(self):
        if self.dirty:
            #draw over old position
            game = Game()
            #area calculation
            (x,y) = self.oldpos
            area0 = self.image.get_rect()
            area = pygame.Rect(x,y, x+area0.w, y+area0.h)
            self.drawsurface.blit(game.board.cleansurface, self.oldpos, area)
            #blit new position
            self.drawsurface.blit(self.image, self.screenpos)
            self.clean()
            print "Drawing cursor to " + str(self.drawsurface) + " at " + str(self.screenpos)

    def move(self, (x,y)):
        #note that x and y are _offsets_
        #get handle to gameboard
        game = Game()
        #if uilock is true, we may assume that the offset refers
        #to the board position
        if self.uilock:
            (x0, y0) = self.boardpos
            i = x + x0
            j = y + y0
            if game.board.board[i][j].ownership != Cell.blocked:
                self.boardpos = (i, j)
        else:
            (x0, y0) = self.screenpos
            i = x + x0
            j = y + y0
            if i >= 0 and i <= 640 and j >= 0 and j <= 480:
                self.screenpos = (i,j)
        
    def lock(self):
        self.uilock = True

    def unlock(self):
        self.uilock = False

    def clean(self):
        self._dirty = False

    @property
    def screenpos(self):
        return self._screenpos

    @screenpos.setter
    def screenpos(self, value):
        self._dirty = True
        self.oldpos = self._screenpos
        self._screenpos = value

    @property
    def boardpos(self):
        return self._boardpos
    
    @boardpos.setter
    def boardpos(self, value):
        self._dirty = True
        #automatically calculate cursor screen position from 
        #the board position
        (i,j) = value
        game = Game()
        r = game.board.cellradius
        screenx = int(2 * r * j + r * i + game.board.margins[0])
        screeny = int(float(r) * sqrt(3) * i + game.board.margins[1])
        self.screenpos = (screenx, screeny)
        self._boardpos = value

    @property
    def dirty(self):
        return self._dirty
