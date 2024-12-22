"""
Given an array arr[] of size n, find all the Leaders in the array.
An element is a Leader if it is greater than
or equal to all the elements to its right side.

Note: The rightmost element is always a leader.

Examples:
Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: 17 is greater than all the elements to its right - [4, 3, 5, 2],
thus 17 is a leader. 5 is greater than all the elements to its right - [2],
thus 5 is a leader. 2 has no element to its right, thus 2 is a leader.


Input: arr[] = [1, 2, 3, 4, 5, 2]
Output: [5, 2]
Explanation: 5 is greater than all the elements to its right - [2],
thus 5 is a leader. 2 has no element to its right, therefore 2 is a leader.
"""


def array_leaders(array: list[int]) -> list[int]:
    *items, leader = array
    leaders = [leader]
    for item in reversed(items):
        if item >= leader:
            leader = item
            leaders.insert(0, leader)

    return leaders


if __name__ == "__main__":
    given = [16, 17, 4, 3, 5, 2]
    result = array_leaders(given)
    print(result)
