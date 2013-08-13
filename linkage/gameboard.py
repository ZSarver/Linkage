#gameboard.py contains the gameboard and all classes owned by the gameboard
from drawing import draw_hexagon, draw_arc
from math import sqrt

class Gameboard:
    """The gameboard is basically a 9 x 17 array of cells.

    margins is a pair of floats [horizontal,vertical], where 0 \leq horizontal < 1
    is the percentage of the screen to reserve for the horizontal margins, and
    likewise for vertical."""
    #enumerated directions
    upleft = 0
    upright = 1
    right = 2
    downright = 3
    downleft = 4
    left = 5
    
    def __init__(self, surface = None):
        self.board = []
        self.surface = surface
        assert(surface is not None)
       
        for i in range(9):
            self.board.append([])
            for j in range(17):
                self.board[i].append(Cell())                
        #apply ownership and place corners
        initial_ownership = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,2,2,2,2,1,1,1,1,3,3,3,3,0],
                             [0,0,0,2,2,2,2,2,1,1,1,3,3,3,3,3,0],
                             [0,0,2,2,2,2,2,2,1,1,3,3,3,3,3,3,0],
                             [0,2,2,2,2,2,2,2,1,3,3,3,3,3,3,3,0],
                             [0,2,2,2,2,2,2,1,1,3,3,3,3,3,3,0,0],
                             [0,2,2,2,2,2,1,1,1,3,3,3,3,3,0,0,0],
                             [0,2,2,2,2,1,1,1,1,3,3,3,3,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        #.xx    ..x    ...    ...   ...   .x.
        #.1.    .2x    .3x    .4.   x5.   x6. 
        #...    ...    .x.    xx.   x..   ...
        corner_cells = [[],[(0,1)],[(1,2)],[(2,3)],[(3,4)],[(4,5)],[(5,0)],[]]
        corner_cell_locations = [[0,0,0,0,7,4,4,4,4,4,4,4,4,4,4,4,7],
                                 [0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,5],
                                 [0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
                                 [0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
                                 [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
                                 [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0],
                                 [2,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0],
                                 [2,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0],
                                 [7,1,1,1,1,1,1,1,1,1,1,1,7,0,0,0,0]]
        self.cursor = (4,8)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].ownership = initial_ownership[i][j]
                #place corner cells
                if corner_cell_locations[i][j] != 0:
                    self.board[i][j].cell = corner_cells[corner_cell_locations[i][j]]
        self.margins = [-40,110]
        self.cellradius = 18
    
    def draw(self):
        def drawhelper((i,j), highlight = (0,0,0)):
            #The offsets between the centres of adjacent cells are
            #    v1 = < 2 * r, 0 >
            #    v2 = < r , r * sqrt(3) >
            x = 2 * r * j + r * i + self.margins[0]
            y = float(r) * sqrt(3) * i + self.margins[1]
            self.board[i][j].draw(self.surface,(x,y),self.cellradius, highlight)
        r = self.cellradius
        for i in range(9):
            for j in range(17):
                if self.board[i][j].dirty:
                    if (i + j >= 4) and (i + j <= 20):
                        drawhelper((i,j))
        drawhelper(self.cursor, (255,255,255))
    
    def movecursor(self, direction):
        (i,j) = neighbor(self.cursor, direction)
        if self.board[i][j].ownership != Cell.blocked:
            self.cursor = (i,j)
    
    def neighbor((x,y),direction):
        """neighbor, when given a board position as a 2-tuple, returns the
        position of the neighbor given by the following direction table:

        (x,y) is a board position
        direction is a number 0-5
        .01
        5X2
        43.
        """
        if direction == 0:
            return (x,y-1)
        elif direction == 1:
            return (x+1,y-1)
        elif direction == 2:
            return (x+1,y)
        elif direction == 3:
            return (x,y+1)
        elif direction == 4:
            return (x-1,y+1)
        elif direction == 5:
            return (x-1,y)

class Cell:
    """Cells are the principal components of Gameboards. Each cell
    is actually a graph, with the exits being vertices and the paths
    being edges.

    The vertices of these graphs are the integers 0 through 5. The
    edges are also lists for simplicity. So each graph is a list of
    edges. Up to rotation, there are 5 unique cells. They are
    enumerated below. Cell 0 is the default.

    Note that these are undirected graphs, so the edge [0,3] is the
    same as the edge [3,0].

    """
    cells = [[(0,3),(1,4),(2,5)],[(1,2),(3,4),(5,0)],[(2,3),(4,0),(5,1)],[(0,3),(1,2),(4,5)],[(0,2),(1,4),(3,5)],[]]
    #ownership "enum"
    blocked = 0
    neutral = 1
    player_1 = 2
    player_2 = 3
    #cell type "enum"
    asterisk = 0
    asteroid = 1
    x = 2
    bball_court = 3
    bball = 4
    blank = 5
    def __init__(self, cellid = asterisk):
        self._cell = self.cells[cellid]
        self._ownership = self.blocked
        self._dirty = True

    #The following methods are getters and setters that flip the
    #dirty bit of the cell automatically when certain variables
    #are accessed
    @property
    def cell(self):
        return self._cell
        
    @cell.setter
    def cell(self, value):
        self._dirty = True
        self._cell = value

    @property
    def ownership(self):
        return self._ownership

    @ownership.setter
    def ownership(self, value):
        self._dirty = True
        self._ownership = value
    @property
    def dirty(self):
        return self._dirty

    def clean(self):
        """Sets the dirty bit to false."""
        self._dirty = False
        
    def rotate_clockwise(self):
        """Rotating clockwise is the same as adding 1 (mod 6) to 
        each vertex in each edge of a cell."""
        for i in range(len(self.cell)):
            for j in range(2):
                self.cell[i][j] = (self.cell[i][j]+1) % 6
                
    def rotate_counterclockwise(self):
        """Rotating counterclockwise is the same as subtracting 1 (mod 6) to
        each vertex in each edge of a cell."""
        for i in range(len(self.cell)):
            for j in range(2):
                self.cell[i][j] = (self.cell[i][j]-1) % 6
                
    def draw(self, surface, (x, y), radius, outline_color=(0,0,0)):
        #             blocked,     neutral,       p1,           p2
        colors = [(50, 50, 50), (180,133,63), (190,163,63), (205, 133, 93)]
        draw_hexagon(surface, x, y, radius, colors[self.ownership], outline_color)
        arc_color = (0,0,0)
        for p in self.cell:
            draw_arc(surface, x, y, radius, p, arc_color)
        self.clean()