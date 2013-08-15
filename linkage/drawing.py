from math import sqrt
from pygame.gfxdraw import *

import pygame
import os.path

def draw_hexagon(surface, x, y, r, color, border_color):
    """Draws a hexagon centered at (x,y), where 
    r = min{d(x,center) : x \in border} and
    color and border_color are (R,G,B) triples
    """
    points = [(x, int(float(y) - (2.0/sqrt(3.0))*float(r))),
              (x+r, int(float(y) - float(r)/sqrt(3.0))),
              (x+r, int(float(y) + float(r)/sqrt(3.0))),
              (x, int(float(y) + (2.0/sqrt(3.0))*float(r))),
              (x-r, int(float(y) + float(r)/sqrt(3.0))),
              (x-r, int(float(y) - float(r)/sqrt(3.0)))]
    filled_polygon(surface, points, color)
    aapolygon(surface, points, border_color)

def draw_arc(surface, x, y, r, (a,b), color = (0,0,0)):
    #draws a bezier curve through the midpoints of two sides of a hex.
    #the "midpoint" of the bezier curve is always the center of the hex
    #the (a,b) argument determines through which sides the curve is drawn.
    midpoints = [(x-(r/2), y-(r * sqrt(3) / 2)), #side 0
                 (x+(r/2), y-(r * sqrt(3) / 2)), #side 1
                 (x+r, y),                       #side 2
                 (x+(r/2), y+(r * sqrt(3) / 2)), #side 3
                 (x-(r/2), y+(r * sqrt(3) / 2)), #side 4
                 (x-r, y)]                       #side 5
    points = [midpoints[a], (x,y), midpoints[b]]
    bezier(surface, points, 2, color)

class ImageError(Exception):
    """The error that is thrown for when something goes wrong in transferring
    data to a surface."""
    def __init__(self, desc, filename):
        self.value = "Loading file " + filename + " failed with error description: " + desc
    def __str__(self):
        return repr(self.value)

def safeload(filename):
    """Safely loads an image from disc to a surface. Throws an error on fail."""
    #pygame.image.get_extended() returns true on Windows, so we should have
    #no trouble using pygame.image.load() and png images without doing
    #anything terribly fancy
    surf = pygame.image.load(os.path.join('resources', filename)).convert()
    #set the colorkey to the upper-left pixel
    surf.set_colorkey(surf.get_at((0,0)))
    if surf == None:
        raise ImageError("fail", filename)
    return surf
