"""
Given an array arr[] of N distinct elements and a number K,
where K is smaller than the size of the array.
Find the K'th smallest element in the given array.

Examples:
Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4
Output: 10
"""

import heapq


def k_smallest_element(array: list[int], k: int) -> int:
    return sorted(array)[k - 1]


def k_smallest_element_heap(array: list[int], k: int) -> int:
    return heapq.nsmallest(k, array)[-1]


if __name__ == "__main__":
    given = [7, 10, 4, 3, 20, 15]
    result = k_smallest_element(given, 3)
    result_heap = k_smallest_element_heap(given, 3)
    print(result, result_heap)
