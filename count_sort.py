from typing import TypeVar

T = TypeVar("T", int, float, str)


def count_sort(array: list[T]) -> list[T]:
    if not array:
        return []

    max_val, min_val = max(array), min(array)
    size = max_val - min_val + 1

    counts = [0] * size
    output = [0] * len(array)

    for item in array:
        counts[item - min_val] += 1

    for i in range(1, size):
        counts[i] += counts[i - 1]

    for item in reversed(array):
        output[counts[item - min_val] - 1] = item
        counts[item - min_val] -= 1

    return output


if __name__ == "__main__":
    given = [4, -3, 2, 2, 8, -4, -1, 3, 3, 1]
    result = count_sort(given)
    print(result)
