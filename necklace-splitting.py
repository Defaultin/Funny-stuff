"""
Two thieves have stolen a valuable necklace consisting of several
different types of jewels. There are an even number of each type of jewel
and the thieves wish to split each jewel type evenly amongst the two of them.
The catch is that they must do so by splitting the necklace into some number
of contiguous segments and distribute the segments between the two of them.

Here is an example with four jewel types denoted 🔵, 🟢, 💎, and 🔴
(for sapphire, emerald, diamond, and ruby, respectively).
Let's say the necklace is as follows:

```
~🔵~🔵~🔵~🟢~🔵~💎~🟢~🔴~🔵~🔴~🟢~🔵~🔵~🔵~💎~🔴~🟢~🟢~🔴~🟢~💎~🟢~🔴~🔴~💎~🟢~🟢~🟢~
```

There are 8 sapphires, 10 emeralds, 4 diamonds, and 6 rubies.
We can split the necklace as follows:

```
[~🔵~, ~🔵~, ~🔵~🟢~🔵~💎~🟢~🔴~🔵~, ~🔴~🟢~🔵~🔵~🔵~💎~🔴~🟢~🟢~🔴~🟢~💎~🟢~, ~🔴~🔴~💎~🟢~🟢~🟢~]
```

Then if we give the first, third, and fifth segments to one thief
and the second and fourth segments to the other thief,
each will end up with 4 sapphires, 5 emeralds, 2 diamonds, and 3 rubies:

```
~🔵~    ~🔵~🟢~🔵~💎~🟢~🔴~🔵]~                                     ~🔴~🔴~💎~🟢~🟢~🟢~
    ~🔵~                     ~🔴~🟢~🔵~🔵~🔵~💎~🔴~🟢~🟢~🔴~🟢~💎~🟢]~
```

Using 0-indexing, these cuts occur at the indices [1,2,9,22].
"""

from collections import Counter
from enum import Enum
from itertools import combinations
from random import sample, shuffle
from typing import Generator


class Jewel(Enum):
    DIAMOND = "💎"
    RUBY = "🔴"
    ONYX = "⚫"
    TOPAZ = "🟡"
    PEARL = "⚪"
    QUARTZ = "🟤"
    EMERALD = "🟢"
    CITRINE = "🟠"
    SAPPHIRE = "🔵"
    AMETHYST = "🟣"


class Necklace:
    def __init__(self, jewels: list[Jewel]) -> None:
        if not jewels:
            raise ValueError("Empty necklace")

        self._cuts = len(jewels) - 1
        self._jewels = jewels

    @property
    def jewels(self) -> list[Jewel]:
        return self._jewels

    def __repr__(self) -> str:
        return "~" + "~".join(jewel.value for jewel in self._jewels) + "~"

    def __len__(self) -> int:
        return len(self._jewels)

    def cut(self, indexes: list[int]) -> list["Necklace"]:
        if not all(0 <= index < self._cuts for index in indexes):
            raise ValueError(f"Indexes out of range: [0, {self._cuts - 1}]")

        necklaces, start = [], 0
        for index in sorted(indexes):
            necklaces.append(Necklace(self._jewels[start:index + 1]))
            start = index + 1

        if start <= self._cuts:
            necklaces.append(Necklace(self._jewels[start:]))

        return necklaces

    def get_all_cuts(self) -> Generator[list["Necklace"], None, None]:
        for length in range(1, self._cuts):
            for cuts in combinations(range(self._cuts), length):
                yield self.cut(list(cuts))


def is_fair_division(necklaces: list[Necklace], quantity: int) -> bool:
    divisions = [necklaces[i::quantity] for i in range(quantity)]
    jewel_counts = [
        sum((Counter(necklace.jewels) for necklace in necklaces), Counter())
        for necklaces in divisions
    ]

    return all(counts == jewel_counts[0] for counts in jewel_counts)


def minimum_fair_cuts(necklace: Necklace, quantity: int) -> list[Necklace]:
    solution, minimum = None, len(necklace)

    for cuts in necklace.get_all_cuts():
        if is_fair_division(cuts, quantity) and len(cuts) < minimum:
            solution, minimum = cuts, len(cuts)

    if solution is None:
        raise ValueError("No fair division found")

    return solution


def split_necklace() -> None:
    thieves = 2
    gems_per_thieve = 6
    jewels = thieves * sample(gems_per_thieve * list(Jewel), gems_per_thieve)
    shuffle(jewels)
    necklace = Necklace(jewels)
    result = minimum_fair_cuts(necklace, thieves)
    print("Initial condition:", necklace)
    print("Solution:", result)
    print("Minimum number of cuts:", len(result) - 1)


if __name__ == "__main__":
    split_necklace()
