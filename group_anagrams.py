"""
Given an array of strings, group the anagrams together.
You can return the answer in any order.

Examples:
Input: strings = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strings that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can form each other.
The strings "ate", "eat", and "tea" are anagrams as they can form each other.

Input: strings = [""]
Output: [[""]]

Input: strings = ["a"]
Output: [["a"]]
"""

from collections import defaultdict


def group_anagrams(strings):
    anagrams = defaultdict(list)

    for string in strings:
        sorted_string = "".join(sorted(string))
        anagrams[sorted_string].append(string)

    return list(anagrams.values())


if __name__ == "__main__":
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strings))
