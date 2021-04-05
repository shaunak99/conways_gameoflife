import numpy as np
import time

class Cell:
    """
    Object representing each cell
    """
    def __init__(self,x,y,state):
        self.pose = [x,y]
        self.neighbours = []
        self.alive = state

    def get_neighbours(self,grid,shape):
        """
        Function to find all neighbouring cells
        NOTE: Wrap-around has not been implemented in this
        """
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                if (self.pose[0] == 0 and i == 0) or (self.pose[0] == shape[0]-1 and i == 2):
                    self.neighbours.append(0)
                elif (self.pose[1] == 0 and j == 0) or (self.pose[1] == shape[1]-1 and j == 2):
                    self.neighbours.append(0)
                else:
                    self.neighbours.append(grid[self.pose[0]+i-1][self.pose[1]+j-1])

    def compute_state(self):
        """
        Compute state as dead or alive for each cell
        """
        sum = np.sum(self.neighbours)

        if self.alive and ((sum == 3) or (sum == 2)):
            self.alive = True
        elif (self.alive == False) and (sum == 3):
            self.alive = True
        else:
            self.alive = False

        self.neighbours = []
        return (self.pose,int(self.alive))


def create_cells(grid,shape):
    """
    Create cell object for each grid cell
    """

    cells = [[None for _ in range(shape[1])] for _ in range(shape[0])]

    for i in range(shape[0]):
        for j in range(shape[1]):
            cells[i][j] = Cell(i,j,bool(grid[i][j]))

    return cells


def run_generation(cells,grid,shape):
    """
    Run 1 generation
    """

    for row in cells:
        for cell in row:
            cell.get_neighbours(grid, shape)

    for row in cells:
        for cell in row:
            (i,j),state = cell.compute_state()
            grid[i][j] = state

def create_display(ele):
    """
    "#" - Represents live cells
    " " - Represents dead cells
    """
    if(ele == 1):
        return "#"
    else:
        return " "


def display(grid):
    """
    Display cells.
    """
    gdisp= np.array([[create_display(e) for e in row] for row in grid])
    gdisp = np.array2string(gdisp,separator='',formatter={'str_kind': lambda x: x})
    print(gdisp)


def run(grid,generations):
    """
    Run calls all the functions and shows the game of life simulation in action.
    The grid shape is fixed in this application to (20,50).
    """

    shape = grid.shape      #grid shap fixed as (20,50)
    cells = create_cells(grid,shape)

    print("\033c")          #To refresh display
    display(grid)
    for _ in range(generations):
        run_generation(cells,grid,shape)
        time.sleep(0.5)
        print("\033c")
        display(grid)


if __name__ == "__main__":
    run()
