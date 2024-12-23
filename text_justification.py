"""
Given an array of strings words and a width maxWidth,
format the text such that each line has exactly maxWidth
characters and is fully (left and right) justified.

You should pack your words in a greedy approach;
that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line does not divide evenly between words,
empty slots on the left will be assigned more spaces than slots on the right.

For the last line of text, it should be left-justified,
and no extra space is inserted between words.

Notes:
A word is defined as a character sequence consisting of non-space chars only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Examples:

Input:
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    max_width = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Input:
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    max_width = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

Input:
    words = [
        "Science", "is", "what", "we", "understand", "well", "enough",
        "to", "explain", "to", "a", "computer.",
        "Art", "is", "everything", "else", "we", "do"
    ]
    max_width = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""


def fill_spaces(
    line: list[str], max_width: int, is_last: bool = False,
) -> list[str]:
    if is_last or len(line) == 1:
        return " ".join(line).ljust(max_width)

    total_spaces = max_width - sum(len(word) for word in line)
    spaces_between_words, extra_spaces = divmod(total_spaces, len(line) - 1)

    for i in range(extra_spaces):
        line[i] += " "

    return (" " * spaces_between_words).join(line)


def justify_text(words: list[str], max_width: int) -> list[str]:
    line, text = [], []
    length = 0

    for word in words:
        if length + len(word) + len(line) > max_width:
            text.append(fill_spaces(line, max_width))
            line, length = [], 0

        line.append(word)
        length += len(word)

    text.append(fill_spaces(line, max_width, is_last=True))

    return text


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    print(justify_text(words, 16))
