"""
Write an algorithm to determine if a number n is happy.
Return true if n is a happy number, and false if not.
A happy number is a number defined by the following process:
* Starting with any positive integer,
    replace the number by the sum of the squares of its digits.
* Repeat the process until the number equals 1 (where it will stay),
    or it loops endlessly in a cycle which does not include 1.
* Those numbers for which this process ends in 1 are happy.

Examples:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""


def is_happy(n: int) -> bool:
    def sum_of_squares(num: int) -> int:
        return sum(int(digit) ** 2 for digit in str(num))

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)

    return n == 1


if __name__ == "__main__":
    print(is_happy(2) is False)
    print(is_happy(7) is True)
    print(is_happy(19) is True)
    print(is_happy(1111111) is True)
