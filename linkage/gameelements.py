class Cell:
    """Cells are the principal components of Gameboards. Each cell
    is actually a graph, with the exits being vertices and the paths
    being edges.

    The vertices of these graphs are the integers 0 through 5. The 
    edges are tuples. So each graph is a list of edges. Up to rotation,
    there are 5 unique cells. They are enumerated below. Cell 0 is the
    default."""
    cells = [[(0,3),(1,4),(2,5)],[(1,2),(3,4),(5,0)],[(2,3),(4,0),(5,1)],[(0,3),(1,2),(4,5)],[(0,2),(1,4),(3,5)]]
    def __init__(self, cellid = 0):
        self.cell = self.cells[cellid]

class Gameboard:
    """The gameboard is basically a 7 x 15 array of cells."""
    def __init__(self):
        self.board = []
        for i in range(7):
            self.board.append([])
            for j in range(15):
                self.board[i].append(Cell())
