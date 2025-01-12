import numpy as np


class IslandMap:
    def __init__(self, matrix: list[list[bool]]) -> None:
        self.islands = 0
        self.grid = np.array(matrix, dtype=np.bool_)
        self.rows, self.cols = self.grid.shape
        self.visited = np.zeros(self.grid.shape, dtype=np.bool_)
        self.directions = [
            (-1, 1),  (0, 1),  (1, 1),
            (-1, 0),           (1, 0),
            (-1, -1), (0, -1), (1, -1)
        ]

    def is_land(self, i: int, j: int) -> bool:
        return (
            0 <= i < self.rows and 0 <= j < self.cols
            and not self.visited[i, j] and self.grid[i, j]
        )

    def dfs(self, i: int, j: int) -> None:
        self.visited[i, j] = True
        for dx, dy in self.directions:
            x, y = i + dx, j + dy
            if self.is_land(x, y):
                self.dfs(x, y)

    def count_islands(self) -> int:
        for i in range(self.rows):
            for j in range(self.cols):
                # If a cell with value 1 is not visited yet, then island found
                if self.grid[i, j] and not self.visited[i, j]:
                    # Visit all cells in this island and increment island count
                    self.dfs(i, j)
                    self.islands += 1

        return self.islands


if __name__ == "__main__":
    grid = np.random.choice([0, 0, 1], size=(10, 10))
    print(grid)
    print("Islands =", IslandMap(grid).count_islands())
