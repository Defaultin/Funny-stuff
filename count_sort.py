from typing import TypeVar

T = TypeVar("T", int, float, str)


def count_sort(array: list[T]) -> list[T]:
    if not array:
        return []

    max_val, min_val = max(array), min(array)
    size = max_val - min_val + 1
    counts = [0] * size
    output = []

    for item in array:
        counts[item - min_val] += 1

    for index in range(size):
        output.extend([index + min_val] * counts[index])

    return output


if __name__ == "__main__":
    given = [4, -3, 2, 2, 8, -4, -1, 3, 3, 1]
    result = count_sort(given)
    print(result)
