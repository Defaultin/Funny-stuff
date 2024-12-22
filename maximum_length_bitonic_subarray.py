"""
Given an array A[0, ..., n - 1] containing n positive integers,
a subarray A[i, ..., j] is bitonic if there is a k with i <= k <= j
such that A[i] <= A[i + 1] ... = A[k + 1] >= ... A[j - 1] >= A[j].
Write a function that takes an array as argument and returns the length
of the maximum length bitonic subarray.

Examples:
Input: A[] = {12, 4, 78, 90, 45, 23}
Output: 5
Explanation: The maximum length bitonic subarray is {4, 78, 90, 45, 23}.

Input: A[] = {20, 4, 1, 2, 3, 4, 2, 10}
Output: 5
Explanation: The maximum length bitonic subarray is {1, 2, 3, 4, 2}.

Input: A[] = {10}
Output: 1
Explanation: The single element is bitonic, so output is 1.

Input: A[] = {10, 20, 30, 40}
Output: 4
Explanation: The complete array itself is bitonic, so output is 4.

Input: A[] = {40, 30, 20, 10}
Output: 4
Explanation: The complete array itself is bitonic, so output is 4.
"""


def maximum_length_bitonic_subarray(array: list[int]) -> int:
    n = len(array)
    left, right = [1] * n, [1] * n

    for i in range(1, n):
        if array[i] >= array[i - 1]:
            left[i] = left[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if array[i] >= array[i + 1]:
            right[i] = right[i + 1] + 1

    max_length = 1
    for i in range(1, n):
        max_length = max(max_length, left[i] + right[i] - 1)

    return max_length


if __name__ == "__main__":
    given = [20, 4, 1, 2, 3, 4, 2, 10]
    result = maximum_length_bitonic_subarray(given)
    print(result)
