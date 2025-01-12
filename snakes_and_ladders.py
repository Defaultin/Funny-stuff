"""
You are given an n x n integer matrix board where the cells are labeled
from 1 to n^2 in a Boustrophedon style starting from the bottom left
of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board.
In each move, starting from square curr, do the following:
* Choose a destination square next with a label
    in the range [curr + 1, min(curr + 6, n^2)].
    This choice simulates the result of a standard 6-sided die roll:
    i.e., there are always at most 6 destinations,
    regardless of the size of the board.
* If next has a snake or ladder,
    you must move to the destination of that snake or ladder.
    Otherwise, you move to next.
* The game ends when you reach the square n^2.

A square on row r and column c has a snake or ladder if board[r][c] != -1.
The destination of that snake or ladder is board[r][c].
Squares 1 and n^2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll.
If the destination to a snake or ladder is a start of another snake or ladder,
you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]],
and on the first move, your destination square is 2.
You follow the ladder to square 3,
but do not follow the subsequent ladder to 4.

Return the least number of dice rolls required to reach the square n^2.
If it is not possible to reach the square, return -1.

Examples:

Input: board = [
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,35,-1,-1,13,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,15,-1,-1,-1,-1]
]
Output: 4
Explanation:
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square.

Input: board = [[-1,-1],[-1,3]]
Output: 1
"""


from collections import deque


def snakes_and_ladders(board: list[list[int]]) -> int:
    n = len(board)
    target = n * n
    visited = [False] * target
    queue = deque([(1, 0)])

    def get_board_value(position: int) -> int:
        quot, rem = divmod(position - 1, n)
        row = n - 1 - quot
        col = rem if quot % 2 == 0 else n - 1 - rem
        return board[row][col]

    while queue:
        position, moves = queue.popleft()
        if position == target:
            return moves

        if visited[position - 1]:
            continue

        visited[position - 1] = True
        dice_range = range(position + 1, min(position + 7, target + 1))
        for next_position in dice_range:
            if (board_value := get_board_value(next_position)) != -1:
                next_position = board_value

            if not visited[next_position - 1]:
                queue.append((next_position, moves + 1))

    return -1


if __name__ == "__main__":
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]
    print(snakes_and_ladders(board))

    board = [
        [-1, -1, 19, 10, -1],
        [2, -1, -1, 6, -1],
        [-1, 17, -1, 19, -1],
        [25, -1, 20, -1, -1],
        [-1, -1, -1, -1, 15]
    ]
    print(snakes_and_ladders(board))

    board = [[-1, -1], [-1, 3]]
    print(snakes_and_ladders(board))
