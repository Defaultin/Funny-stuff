"""
Given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container,
such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Examples:
8|    █              █      
7|    █~~~~~~~~~~~~~~█~~~~~█
6|    █~~█~~~~~~~~~~~█~~~~~█
5|    █~~█~~~~~█~~~~~█~~~~~█
4|    █~~█~~~~~█~~█~~█~~~~~█
3|    █~~█~~~~~█~~█~~█~~█~~█
2|    █~~█~~█~~█~~█~~█~~█~~█
1| █  █~~█~~█~~█~~█~~█~~█~~█
0|--------------------------
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (~) the container can contain is 49.
"""


def most_water(height: list[int]) -> int:
    max_water = 0
    left, right = 0, len(height) - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(most_water(height))
