"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Examples:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
"""


def climb_stairs(n: int) -> int:
    if n == 1:
        return 1

    _1, _2 = 1, 2
    for _ in range(3, n + 1):
        _3 = _1 + _2
        _1, _2 = _2, _3

    return _2


if __name__ == "__main__":
    result = climb_stairs(2)
    print(result)
