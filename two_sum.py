"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

Examples:
Input: numbers = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because numbers[0] + numbers[1] == 9, we return [0, 1].

Input: numbers = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: numbers = [3,3], target = 6
Output: [0,1]
"""


def two_sum(numbers: list[int], target: int) -> list[int]:
    indexes = {}

    for i, num in enumerate(numbers):
        if target - num in indexes:
            return [indexes[target - num], i]

        indexes[num] = i


def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1


def three_sum(numbers: list[int], target: int) -> list[list[int]]:
    numbers.sort()
    result = []

    for i in range(len(numbers) - 2):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        left, right = i + 1, len(numbers) - 1

        while left < right:
            total = numbers[i] + numbers[left] + numbers[right]

            if total == target:
                result.append([numbers[i], numbers[left], numbers[right]])

                while left < right and numbers[left] == numbers[left + 1]:
                    left += 1

                while left < right and numbers[right] == numbers[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    given = [2, 7, 11, 15]
    result = two_sum(given, 9)
    print(result)

    result = two_sum_sorted(given, 9)
    print(result)

    given = [-1, 0, 1, 2, -1, -4]
    result = three_sum(given, 0)
    print(result)
