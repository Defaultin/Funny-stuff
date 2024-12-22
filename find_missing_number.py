"""
Given an array arr[] of size n-1 with integers in the range of [1, n],
the task is to find the missing number from the first n integers.

Note: There are no duplicates in the list.

Examples:

Input: arr[] = [1, 2, 4, 6, 3, 7, 8] , n = 8
Output: 5
Explanation: Here the size of the array is 8, so the range will be [1, 8].
The missing number between 1 to 8 is 5.

Input: arr[] = [1, 2, 3, 5], n = 5
Output: 4
Explanation: Here the size of the array is 4, so the range will be [1, 5].
The missing number between 1 to 5 is 4.
"""


def find_missing_number(array: list[int]) -> int:
    n = len(array) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(array)
    return expected_sum - actual_sum


def find_missing_number_xor(array: list[int]) -> int:
    xor1 = array[0]
    xor2 = 1

    for item in array[1:]:
        xor1 ^= item

    for item in range(2, len(array) + 2):
        xor2 ^= item

    return xor1 ^ xor2


if __name__ == "__main__":
    given = [1, 2, 4, 6, 3, 7, 8]
    result = find_missing_number(given)
    result_xor = find_missing_number_xor(given)
    print(result, result_xor)
