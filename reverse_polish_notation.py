"""
You are given an array of strings tokens that represents an arithmetic
expression in a Reverse Polish Notation. Evaluate the expression.
Return an integer that represents the value of the expression.

Note that:
* The valid operators are '+', '-', '*', and '/'.
* Each operand may be an integer or another expression.
* The division between two integers always truncates toward zero.
* There will not be any division by zero.
* The input represents a valid expression in a reverse polish notation.
* The answer and all the intermediate calculations are integers.

Examples:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22
"""


def eval_rpn(tokens: list[str]) -> int:
    stack = []
    operators = {
        "+": int.__add__,
        "-": int.__sub__,
        "*": int.__mul__,
        "/": int.__truediv__,
    }

    for token in tokens:
        if token in operators:
            right_operand, left_operand = stack.pop(), stack.pop()
            stack.append(int(operators[token](left_operand, right_operand)))
        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == "__main__":
    array = ["2", "1", "+", "3", "*"]
    print(eval_rpn(array))

    array = ["4", "13", "5", "/", "+"]
    print(eval_rpn(array))

    array = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(eval_rpn(array))
