"""
Find the length of the longest substring without repeating characters.

Examples:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
"""


def longest_substring_without_repeats(string: str) -> int:
    left = right = max_len = 0
    chars = set()

    while right < len(string):
        if string[right] in chars:
            chars.remove(string[left])
            left += 1
        else:
            chars.add(string[right])
            max_len = max(max_len, right - left + 1)
            right += 1

    return max_len


if __name__ == "__main__":
    print(longest_substring_without_repeats("abcabcbb"))
    print(longest_substring_without_repeats("bbbbb"))
    print(longest_substring_without_repeats("pwwkew"))
