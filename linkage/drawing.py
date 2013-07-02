from math import sqrt
from pygame.gfxdraw import *

def draw_hexagon(surface, x, y, r, color, border_color):
    """Draws a hexagon centered at (x,y), where 
    r = min{d(x,center) : x \in border} and
    color and border_color are (R,G,B) triples
    """
    points = [(int(float(x) + float(r)/sqrt(3)),y-r),
              (int(float(x) + float(r) * (sqrt(3)/2.0)), y),
              (int(float(x) + float(r)/sqrt(3)),y+r),
              (int(float(x) - float(r)/sqrt(3)),y+r),
              (int(float(x) - float(r) * (sqrt(3)/2.0)), y),
              (int(float(x) - float(r)/sqrt(3)),y-r)]
    filled_polygon(surface, points, color)
    aapolygon(surface, points, border_color)
