"""
The string "PAYPALISHIRING" is written in a zigzag pattern
on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR".
Take a string and make this conversion given a number of rows.

Examples:
Input: string = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Explanation:
P   A   H   N
A P L S I I G
Y   I   R

Input: string = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Input: string = "A", numRows = 1
Output: "A"
"""


def zigzag_string(string: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(string):
        return string

    rows = [""] * num_rows
    current_row = 0
    going_down = -1

    for char in string:
        rows[current_row] += char
        if current_row == 0 or current_row == num_rows - 1:
            going_down *= -1
        current_row += going_down

    return "".join(rows)


if __name__ == "__main__":
    text = "PAYPALISHIRING"
    print(zigzag_string(text, 3))
    print(zigzag_string(text, 4))
