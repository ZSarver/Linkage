from math import sqrt
from pygame.gfxdraw import *

def draw_hexagon(surface, x, y, r, color, border_color):
    """Draws a hexagon centered at (x,y), where 
    r = min{d(x,center) : x \in border} and
    color and border_color are (R,G,B) triples
    """
    points = [(x+r, int(float(y) - float(r)/sqrt(3))),
              (x+r, int(float(y) + float(r)/sqrt(3))),
              (x, int(float(y) - float(r) * (2.0/sqrt(3)))),
              (x-r, int(float(y) + float(r)/sqrt(3))),
              (x-r, int(float(y) - float(r)/sqrt(3))),
              (x, int(float(y) + float(r) * (2.0/sqrt(3))))]
    filled_polygon(surface, points, color)
    aapolygon(surface, points, border_color)
