"""
Given an integer array, the task is to find maximum product of any subarray.

Examples:
Input: arr[] = {-2, 6, -3, -10, 0, 2}
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10}, product = 180.

Input: arr[] = {-1, -3, -10, 0, 60}
Output: 60
Explanation: The subarray with maximum product is {60}.
"""


def maximum_product_subarray(array: list[int]) -> int:
    max_product = min_product = absolute = array[0]

    for item in array[1:]:
        if item < 0:
            max_product, min_product = min_product, max_product

        max_product = max(item, max_product * item)
        min_product = min(item, min_product * item)
        absolute = max(absolute, max_product)

    return absolute


if __name__ == "__main__":
    given = [-2, 6, -3, -10, 0, 2]
    result = maximum_product_subarray(given)
    print(result)
