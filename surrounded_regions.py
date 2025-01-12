"""
Given an m x n matrix board containing letters 'X' and 'O',
capture regions that are surrounded:
Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells
    if you can connect the region with 'X' cells
    and none of the region cells are on the edge of the board.

Examples:
Input: board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]
Output: [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","O","X","X"]
]
"""


class RegionsMap:
    def __init__(self, matrix: list[list[str]]) -> None:
        self.grid = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]

    def is_part_of_region(self, row: int, col: int) -> bool:
        return (
            0 <= row < self.rows and 0 <= col < self.cols
            and self.grid[row][col] == "O"
        )

    def dfs(self, row: int, col: int) -> None:
        if self.is_part_of_region(row, col):
            self.grid[row][col] = "T"
            for dx, dy in self.directions:
                self.dfs(row + dx, col + dy)

    def surround_regions(self) -> None:
        for row in range(self.rows):
            for col in range(self.cols):
                is_edge = row in {0, self.rows-1} or col in {0, self.cols-1}
                if is_edge and self.grid[row][col] == "O":
                    self.dfs(row, col)

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == "T":
                    self.grid[row][col] = "O"
                elif self.grid[row][col] == "O":
                    self.grid[row][col] = "X"


if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    regions_map = RegionsMap(board)
    regions_map.surround_regions()
    print(board)
