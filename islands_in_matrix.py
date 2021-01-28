import numpy as np


class Graph:
    '''Count islands in boolean 2D matrix'''
    def __init__(self, grid):
        self.rows, self.cols = grid.shape
        self.grid = grid.copy()
        self.row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        self.col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        self.islands = 0


    def isSafe(self, i, j, visited):
        return (
            i >= 0 and
            i < self.rows and
            j >= 0 and
            j < self.cols and
            not visited[i, j] and
            self.grid[i, j]
        )
            

    def DFS(self, i, j, visited):
        visited[i, j] = True
        for k in range(8):
            ii, jj = i + self.row_nbr[k], j + self.col_nbr[k]
            if self.isSafe(ii, jj, visited):
                self.DFS(ii, jj, visited)


    def countIslands(self):
        visited = np.zeros((self.rows, self.cols), dtype=np.bool_)

        for i in range(self.rows):
            for j in range(self.cols):
                # If a cell with value 1 is not visited yet, then new island found
                if self.grid[i, j] and not visited[i, j]:
                    # Visit all cells in this island and increment island count
                    self.DFS(i, j, visited)
                    self.islands += 1

        return self.islands



if __name__ == '__main__':
    grid = np.random.choice([0, 0, 1], size=(10, 10))
    print(grid)
    print('Islands =', Graph(grid).countIslands())