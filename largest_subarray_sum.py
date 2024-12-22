"""
Given an array arr[], the task is to find the subarray
that has the maximum sum and return its sum.

Examples:

Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

Input: arr[] = {-2, -4}
Output: -2
Explanation: The subarray {-2} has the largest sum -2.

Input: arr[] = {5, 4, 1, 7, 8}
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.
"""


def largest_subarray_sum(array: list[int]) -> int:
    max_sum = max_end = array[0]

    for item in array[1:]:
        max_end = max(item, max_end + item)
        max_sum = max(max_sum, max_end)

    return max_sum


if __name__ == "__main__":
    given = [2, 3, -8, 7, -1, 2, 3]
    result = largest_subarray_sum(given)
    print(result)
