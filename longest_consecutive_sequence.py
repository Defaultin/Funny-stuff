"""
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Examples:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4].

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8].
"""


def longest_consecutive_sequence(nums: list[int]) -> int:
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive_sequence(nums))

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longest_consecutive_sequence(nums))
