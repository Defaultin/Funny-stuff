"""
Given an Array of size N and a value K,
around which we need to right rotate the array.
How do you quickly print the right rotated array?

Examples:
Input: Array[] = {1, 3, 5, 7, 9}, K = 2.
Output: {7, 9, 1, 3, 5}
Explanation:
    After 1st rotation - {9, 1, 3, 5, 7}
    After 2nd rotation - {7, 9, 1, 3, 5}

Input: Array[] = {1, 2, 3, 4, 5}, K = 4.
Output: {2, 3, 4, 5, 1}
"""


def rotate_array(array: list[int], k: int) -> list[int]:
    k = k % len(array)
    return array[-k:] + array[:-k]


if __name__ == "__main__":
    given = [1, 3, 5, 7, 9]
    result = rotate_array(given, 2)
    print(result)
