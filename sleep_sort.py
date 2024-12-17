import asyncio
import random
from typing import Iterable, TypeVar

T = TypeVar("T")


def sleep_sort(iterable: Iterable[T], delay: float = 1e-3) -> list[T]:
    left, right = [], []

    async def _populate(item: T) -> None:
        await asyncio.sleep(abs(item) * delay)
        left.append(item) if item < 0 else right.append(item)

    async def _sort() -> None:
        await asyncio.gather(*(_populate(item) for item in iterable))

    asyncio.run(_sort())
    return left[::-1] + right


def main():
    array = random.sample(range(-1000, 1000), 100)
    result = sleep_sort(array, delay=1 / max(array))
    print(result)
    assert result == sorted(array)


if __name__ == "__main__":
    main()
