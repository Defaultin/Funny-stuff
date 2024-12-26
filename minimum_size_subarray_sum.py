"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is >= to target.
If there is no such subarray, return 0 instead.

Examples:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the constraint.

Input: target = 4, nums = [1,4,4]
Output: 1

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""


def min_subarray_len(numbers: list[str], target: int) -> int:
    left = right = total = 0
    min_len = float("inf")

    while right < len(numbers):
        total += numbers[right]
        right += 1

        while total >= target:
            min_len = min(min_len, right - left)
            total -= numbers[left]
            left += 1

    return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    print(min_subarray_len([2, 3, 1, 2, 4, 3], 7))
    print(min_subarray_len([1, 4, 4], 4))
    print(min_subarray_len([1, 1, 1, 1, 1, 1, 1, 1], 11))
