"""
Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].
You must write an algorithm that runs in O(n) time and without the division.

Examples:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n
    prefix = suffix = 1

    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


if __name__ == "__main__":
    given = [1, 2, 3, 4]
    result = product_except_self(given)
    print(result)
