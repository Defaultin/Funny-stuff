"""
The board is made up of an m x n grid of cells,
where each cell has an initial state:
live (represented by a 1) or dead (represented by a 0).
Each cell interacts with its eight neighbors
using the following four rules:
* Any live cell with fewer than two live neighbors dies.
* Any live cell with two or three live neighbors lives.
* Any live cell with more than three live neighbors dies.
* Any dead cell with exactly three live neighbors becomes a live cell.
The next state of the board is determined by applying the above rules
simultaneously to every cell in the current state of the m x n grid board.
Given the state of the board, update the board to reflect its next state.

Examples:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
"""


def game_of_life(board: list[list[bool]]) -> list[list[bool]]:
    rows, cols = len(board), len(board[0])
    directions = [
        (1, -1),  (1, 0),  (1, 1),
        (0, -1),           (0, 1),
        (-1, -1), (-1, 0), (-1, 1),
    ]

    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0
            for direction_i, direction_j in directions:
                x, y = i + direction_i, j + direction_j
                if 0 <= x < rows and 0 <= y < cols:
                    live_neighbors += board[x][y] & 1

            if board[i][j] and live_neighbors in {2, 3}:
                board[i][j] = 3

            if not board[i][j] and live_neighbors == 3:
                board[i][j] = 2

    for i in range(rows):
        for j in range(cols):
            board[i][j] >>= 1

    return board


if __name__ == "__main__":
    matrix = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    print(game_of_life(matrix))
    matrix = [[1, 1], [1, 0]]
    print(game_of_life(matrix))
