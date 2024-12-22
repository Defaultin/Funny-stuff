"""
Given an array of n non-negative integers arr[]
representing an elevation map where the width of each bar is 1,
compute how much water it can trap after rain.

Examples:
Input: arr[] = {3, 0, 1, 0, 4, 0, 2}
Output: 10
Explanation: The expected rainwater to be trapped is shown in the above image.

Input: arr[] = {3, 0, 2, 0, 4}
Output: 7
Explanation: We trap 0 + 3 + 1 + 3 + 0 = 7 units.

Input: arr[] = {1, 2, 3, 4}
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides

Input: arr[] = {2, 1, 5, 3, 1, 0, 4}
Output: 9
Explanation: We trap 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units of water.

Input: arr[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
Output: 6
Explanation: We trap 1 + 4 + 1 = 6 units of water.
"""


def trapping_rain_water(array: list[int]) -> int:
    n = len(array)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = array[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], array[i])

    right_max[n - 1] = array[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], array[i])

    trapped_water = 0
    for i in range(1, n - 1):
        trapped_water += min(left_max[i], right_max[i]) - array[i]

    return trapped_water


if __name__ == "__main__":
    given = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = trapping_rain_water(given)
    print(result)
