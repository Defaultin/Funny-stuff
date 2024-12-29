"""
Given an array, the task is to find the subarray
that has the maximum sum and return its sum.

Examples:

Input: array = {2, 3, -8, 7, -1, 2, 3}
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

Input: array = {-2, -4}
Output: -2
Explanation: The subarray {-2} has the largest sum -2.

Input: array = {5, 4, 1, 7, 8}
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.
"""

from typing import Callable


def subarray_sum(array: list[int], predicate: Callable = max) -> int:
    max_sum = max_end = array[0]

    for item in array[1:]:
        max_end = predicate(item, max_end + item)
        max_sum = predicate(max_sum, max_end)

    return max_sum


def circular_subarray_sum(array: list[int]) -> int:
    max_sum = subarray_sum(array, predicate=max)

    if max_sum < 0:
        return max_sum

    max_wrap = sum(array) - subarray_sum(array, predicate=min)

    return max(max_sum, max_wrap)


if __name__ == "__main__":
    given = [2, 3, -8, 7, -1, 2, 3]
    print(subarray_sum(given))

    given = [-2, -4]
    print(subarray_sum(given))

    given = [5, 4, 1, 7, 8]
    print(subarray_sum(given))
