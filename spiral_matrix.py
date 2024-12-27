"""
Given an m * n matrix, return all elements of the matrix in spiral order.
"""


def spiral_matrix(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * cols for _ in range(rows)]
    direction = row = col = 0
    result = []

    for _ in range(rows * cols):
        result.append(matrix[row][col])
        visited[row][col] = True

        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]
        is_row_valid = 0 <= next_row < rows
        is_col_valid = 0 <= next_col < cols

        if is_row_valid and is_col_valid and not visited[next_row][next_col]:
            row, col = next_row, next_col
        else:
            direction = (direction + 1) % 4
            row = row + directions[direction][0]
            col = col + directions[direction][1]

    return result


if __name__ == "__main__":
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiral_matrix(M))
