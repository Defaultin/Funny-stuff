"""
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount cannot be made up by any combination of coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Examples:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0
"""


def coin_change(coins: list[int], amount: int) -> int:
    inf = float("inf")
    dp = [inf] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] != inf:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != inf else -1


if __name__ == "__main__":
    print(coin_change([1, 2, 5], 11))
    print(coin_change([2], 3))
    print(coin_change([1], 0))
