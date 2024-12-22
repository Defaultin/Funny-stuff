"""
Given an array arr[] of size n, return an equilibrium index
(if any) or -1 if no equilibrium index exists.
The equilibrium index of an array is an index
such that the sum of elements at lower indexes
equals the sum of elements at higher indexes.

Note: Return -1 if no such point exists.

Examples:
Input: arr[] = {-7, 1, 5, 2, -4, 3, 0}
Output: 3
Explanation: In 1-based indexing, 4 is an equilibrium index,
because: arr[0] + arr[1] + arr[2] = arr[4] + arr[5] + arr[6]

Input: arr[] = {1, 2, 3}
Output: -1
Explanation: There is no equilibrium index in the array.
"""


def array_equilibrium_index(array: list[int]) -> int:
    n = len(array)
    if n == 1:
        return 0

    prefix_sum = [0] * n
    suffix_sum = [0] * n

    prefix_sum[0] = array[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + array[i]

    suffix_sum[n - 1] = array[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + array[i]

    for i in range(n):
        if prefix_sum[i] == suffix_sum[i]:
            return i

    return -1


if __name__ == "__main__":
    given = [-7, 1, 5, 2, -4, 3, 0]
    result = array_equilibrium_index(given)
    print(result)
