"""
Given an array of points where points[i] = [x_i, y_i]
represents a point on the X-Y plane, return the maximum
number of points that lie on the same straight line.

Examples:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
"""

from collections import defaultdict
from math import gcd


def max_points_on_line(points: list[list[int]]) -> int:
    max_points = 1
    n = len(points)

    if n < 3:
        return n

    for i, (x1, y1) in enumerate(points):
        slope_count = defaultdict(int)
        duplicates = local_max = 0

        for j in range(i + 1, n):
            x2, y2 = points[j]
            dx, dy = x2 - x1, y2 - y1

            if dx == dy == 0:
                duplicates += 1
                continue

            if (g := gcd(dx, dy)) != 0:
                dx //= g
                dy //= g

            if dx < 0:
                dx, dy = -dx, -dy

            if dx == 0:
                dy = 1

            slope_count[dy, dx] += 1
            local_max = max(local_max, slope_count[dy, dx])

        max_points = max(max_points, local_max + duplicates + 1)

    return max_points


if __name__ == "__main__":
    array = [[1, 1], [2, 2], [3, 3]]
    print(max_points_on_line(array))

    array = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print(max_points_on_line(array))
