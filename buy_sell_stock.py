"""
You are given an array prices where prices[i]
is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one
stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Examples:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 5.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


def buy_sell_stock(prices: list[int]) -> int:
    max_profit = 0
    min_price = float("inf")

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


if __name__ == "__main__":
    given = [7, 1, 5, 3, 6, 4]
    result = buy_sell_stock(given)
    print(result)
