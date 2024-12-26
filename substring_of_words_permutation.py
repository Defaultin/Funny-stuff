"""
You are given a string s and an array of strings words.
All the strings of words are of the same length.
A concatenated string is a string that exactly contains
all the strings of any permutation of words concatenated.
Return an array of the starting indices of all the concatenated substrings.

Examples:
Input: string = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"].
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"].

Input: string = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: There is no concatenated substring.

Input: string = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
"""

from collections import Counter


def substring_of_words_permutation(string: str, words: list[str]) -> list[int]:
    if not string or not words:
        return []

    word_count, word_len = len(words), len(words[0])
    word_map = Counter(words)
    indexes = []

    for i in range(word_len):
        count = 0
        left = right = i
        frequencies = Counter()

        while right + word_len <= len(string):
            word = string[right:right + word_len]
            right += word_len

            if word in word_map:
                frequencies[word] += 1
                count += 1

                while frequencies[word] > word_map[word]:
                    left_word = string[left:left + word_len]
                    frequencies[left_word] -= 1
                    count -= 1
                    left += word_len

                if count == word_count:
                    indexes.append(left)
            else:
                frequencies.clear()
                count = 0
                left = right

    return indexes


if __name__ == "__main__":
    s, w = "barfoothefoobarman", ["foo", "bar"]
    print(substring_of_words_permutation(s, w))

    s, w = "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]
    print(substring_of_words_permutation(s, w))

    s, w = "barfoofoobarthefoobarman", ["bar", "foo", "the"]
    print(substring_of_words_permutation(s, w))
