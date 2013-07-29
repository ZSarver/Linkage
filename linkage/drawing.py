from math import sqrt
from pygame.gfxdraw import *

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