"""
There are n children standing in a line.
Each child is assigned a rating value given in the integer array ratings.
You are giving candies to children subjected to the following requirements:
* Each child must have at least one candy.
* Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to distribute to the children.

Examples:
Input: ratings = [1, 0, 2]
Output: 5
Explanation: You can allocate [2, 1, 2] candies respectively.

Input: ratings = [1, 2, 2]
Output: 4
Explanation: You can allocate [1, 2, 1] candies respectively.

Input: ratings = [5, 1, 3, 2, 0, 9, 1, 4]
Output: 14
Explanation: You can allocate [2, 1, 3, 2, 1, 2, 1, 2] candies respectively.
"""


def candy(ratings: list[int]) -> int:
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


if __name__ == "__main__":
    ratings = [5, 1, 3, 2, 0, 9, 1, 4]
    print(candy(ratings))
