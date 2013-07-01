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
    cells = [[(0,3),(1,4),(2,5)],[(1,2),(3,4),(5,0)],[(2,3),(4,0),(5,1)],[(0,3),(1,2),(4,5)],[(0,2),(1,4),(3,5)]]
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
    def __init__(self, cellid = 0):
        self.cell = self.cells[cellid]
        self.ownership = self.blocked
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
        #apply ownership
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].ownership = self.initial_ownership[i][j]
    
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
