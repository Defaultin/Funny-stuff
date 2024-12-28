"""
There are spherical balloons taped onto a flat wall that represents XY-plane.
The balloons are represented as a 2D integer array points where
points[i] = [x_start, x_end] denotes a balloon whose horizontal
diameter stretches between x_start and x_end.
You do not know the exact y-coordinates of the balloons.
Arrows can be shot up directly vertically (in the positive y-direction)
from different points along the x-axis.
A balloon with x_start, x_end is burst by an arrow at x if x_start<=x<=x_end.
There is no limit to the number of arrows that can be shot.
A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
Return the minimum number of arrows that must be shot to burst all balloons.

Examples:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
* Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
* Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: 1 arrow needs to be shot for each balloon for a total of 4 arrows.

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
* Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
* Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
"""


def minimum_arrow_shots(points: list[list[int]]) -> int:
    points.sort()
    intersects = [points[0]]

    for x, y in points[1:]:
        if x <= intersects[-1][1]:
            intersects[-1][0] = max(x, intersects[-1][0])
            intersects[-1][1] = min(y, intersects[-1][1])
        else:
            intersects.append([x, y])

    return len(intersects)


def minimum_arrow_shots_greedy(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[1])
    arrows, current_end = 1, points[0][1]

    for x_start, x_end in points[1:]:
        if x_start > current_end:
            arrows += 1
            current_end = x_end

    return arrows


if __name__ == "__main__":
    array = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(minimum_arrow_shots(array))
    print(minimum_arrow_shots_greedy(array))

    array = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(minimum_arrow_shots(array))
    print(minimum_arrow_shots_greedy(array))

    array = [[1, 2], [2, 3], [3, 4], [4, 5]]
    print(minimum_arrow_shots_greedy(array))
    print(minimum_arrow_shots(array))
