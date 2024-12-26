"""
Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t
(including duplicates) is included in the window.
If there is no such substring, return the empty string "".

Examples:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation:
The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

from collections import Counter, defaultdict


def minimum_window(string: str, pattern: str) -> str:
    if not string or not pattern:
        return ""

    left = right = formed = 0
    window_counts = defaultdict(int)
    required_counts = Counter(pattern)
    required_length = len(required_counts)
    min_length, min_window = float("inf"), None

    while right < len(string):
        char = string[right]
        window_counts[char] += 1

        if char in required_counts and window_counts[char] == required_counts[char]:
            formed += 1

        while left <= right and formed == required_length:
            char = string[left]
            if (length := right - left + 1) < min_length:
                min_length, min_window = length, string[left:right + 1]

            window_counts[char] -= 1
            if char in required_counts and window_counts[char] < required_counts[char]:
                formed -= 1

            left += 1
        right += 1

    return "" if min_length == float("inf") else min_window


if __name__ == "__main__":
    s, t = "ADOBECODEBANC", "ABC"
    print(minimum_window(s, t))

    s, t = "a", "a"
    print(minimum_window(s, t))

    s, t = "a", "aa"
    print(minimum_window(s, t))
