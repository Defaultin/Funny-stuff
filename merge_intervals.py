"""
Given an array of intervals where intervals[i] = [x_i, y_i],
merge all overlapping intervals, and return an array of the
non-overlapping intervals that cover all the intervals in the input.

Examples:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]

    for x, y in intervals[1:]:
        if x <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], y)
        else:
            merged.append([x, y])

    return merged


if __name__ == "__main__":
    array = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge_intervals(array))

    array = [[1, 4], [4, 5]]
    print(merge_intervals(array))
