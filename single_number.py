"""
Given a non-empty array of integers nums,
every element appears twice except for one.
Find that single one.

Examples:
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""


def single_number(nums: list[int]) -> int:
    xor = 0
    for num in nums:
        xor ^= num
    return xor


if __name__ == "__main__":
    given = [2, 2, 1]
    result = single_number(given)
    print(result)
