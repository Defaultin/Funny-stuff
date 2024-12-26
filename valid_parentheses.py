"""
Given a string s containing just the characters '(', ')', '{', '}', '[', ']',
determine if the input string is valid.
An input string is valid if:
* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Examples:
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([])"
Output: true
"""


def valid_parentheses(string: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in string:
        if char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            stack.append(char)

    return not stack


if __name__ == "__main__":
    print(valid_parentheses("()"))
    print(valid_parentheses("()[]{}"))
    print(valid_parentheses("(]"))
    print(valid_parentheses("([])"))
