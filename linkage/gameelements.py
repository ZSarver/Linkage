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
    #          0 : "Asterisk"      1 : "Asteroid"          2 : "X"        3 : "bball court"     4 : "bball"
    cells = [[(0,3),(1,4),(2,5)],[(1,2),(3,4),(5,0)],[(2,3),(4,0),(5,1)],[(0,3),(1,2),(4,5)],[(0,2),(1,4),(3,5)]]

    #cell ownership
    #   0  : "blocked"
    #   1  : "neutral"
    #   2  : "player 1"
    #   3  : "player 2"
    def __init__(self, cellid = 0):
        self.cell = self.cells[cellid]
    def rotate_clockwise(self):
        """Rotating clockwise is the same as adding 1 (mod 5) to 
        each vertex in each edge of a cell."""
        for i in range(len(self.cell)):
            for j in range(2):
                self.cell[i][j] = (self.cell[i][j]+1) % 5
    def rotate_counterclockwise(self):
        """Rotating counterclockwise is the same as subtracting 1 (mod 5) to
        each vertex in each edge of a cell."""
        for i in range(len(self.cell)):
            for j in range(2):
                self.cell[i][j] = (self.cell[i][j]-1) % 5

class Gameboard:
    """The gameboard is basically a 9 x 17 array of cells."""
    initial_ownership = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,2,2,2,2,1,1,1,1,3,3,3,3,0],
                         [0,0,0,2,2,2,2,2,1,1,1,3,3,3,3,3,0],
                         [0,0,2,2,2,2,2,2,1,1,3,3,3,3,3,3,0],
                         [0,2,2,2,2,2,2,2,1,3,3,3,3,3,3,3,0],
                         [0,2,2,2,2,2,2,1,1,3,3,3,3,3,3,0,0],
                         [0,2,2,2,2,2,1,1,1,3,3,3,3,3,0,0,0],
                         [0,2,2,2,2,1,1,1,1,3,3,3,3,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    
    def __init__(self):
        self.board = []
        for i in range(7):
            self.board.append([])
            for j in range(15):
                self.board[i].append(Cell())


def neighbor((x,y),direction):
#(x,y) is a board position
#direction is a number 0-5
#.01
#5X2
#43.
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
