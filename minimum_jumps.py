"""
You are given a 0-indexed array of integers nums of length n.
You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
    0 <= j <= nums[i] and i + j < n
Return the minimum number of jumps to reach nums[n - 1].
The test cases are generated such that you can reach nums[n - 1].

Examples:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [2,3,0,1,4]
Output: 2
"""


def minimum_jumps(nums: list[int]) -> int:
    n = len(nums)
    jumps = end = farthest = 0

    for index in range(n - 1):
        farthest = max(farthest, index + nums[index])

        if index == end:
            jumps += 1
            end = farthest

            if end >= n - 1:
                break

    return jumps


if __name__ == "__main__":
    given = [2, 3, 1, 1, 4]
    print(minimum_jumps(given))
