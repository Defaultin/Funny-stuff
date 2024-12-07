"""
Two thieves have stolen a valuable necklace consisting of several
different types of jewels. There are an even number of each type of jewel
and the thieves wish to split each jewel type evenly amongst the two of them.
The catch is that they must do so by splitting the necklace into some number
of contiguous segments and distribute the segments between the two of them.

Here is an example with four jewel types denoted S, E, D, and R
(for sapphire, emerald, diamond, and ruby, respectively).
Let's say the necklace is as follows:

```
[S,S,S,E,S,D,E,R,S,R,E,S,S,S,D,R,E,E,R,E,D,E,R,R,D,E,E,E]
```

There are 8 sapphires, 10 emeralds, 4 diamonds, and 6 rubies.
We can split the necklace as follows:

```
[[S],[S],[S,E,S,D,E,R,S],[R,E,S,S,S,D,R,E,E,R,E,D,E],[R,R,D,E,E,E]]
```

Then if we give the first, third, and fifth segments to one thief
and the second and fourth segments to the other thief,
each will end up with 4 sapphires, 5 emeralds, 2 diamonds, and 3 rubies:

```
[S],    [S,E,S,D,E,R,S],                            [R,R,D,E,E,E]
    [S],                [R,E,S,S,S,D,R,E,E,R,E,D,E],
```

Using 0-indexing, these cuts occur at the indices [1,2,9,22].
"""

from collections import Counter
from enum import Enum
from itertools import combinations
from random import sample, shuffle


class Jewel(Enum):
    DIAMOND = 1
    RUBY = 2
    SAPPHIRE = 3
    EMERALD = 4
    TOPAZ = 5
    AMETHYST = 6
    AQUAMARINE = 7
    GARNET = 8
    PERIDOT = 9
    OPAL = 10


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
        return "~".join(jewel.name for jewel in self._jewels)

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

    def get_all_cuts(self) -> list["Necklace"]:
        return [
            self.cut(list(cuts))
            for length in range(1, self._cuts)
            for cuts in combinations(range(self._cuts), length)
        ]


def is_fair_division(necklaces: list[Necklace], quantity: int) -> bool:
    divisions = [necklaces[i::quantity] for i in range(quantity)]
    jewel_counts = [
        sum((Counter(necklace.jewels) for necklace in necklaces), Counter())
        for necklaces in divisions
    ]

    return all(counts == jewel_counts[0] for counts in jewel_counts)


def minimum_fair_cuts(necklace: Necklace, quantity: int) -> list[Necklace]:
    minimum_cut_id, minimum_cuts = 0, len(necklace)
    all_necklace_cuts = necklace.get_all_cuts()

    for cut_id, cuts in enumerate(all_necklace_cuts):
        if is_fair_division(cuts, quantity) and len(cuts) < minimum_cuts:
            minimum_cut_id, minimum_cuts = cut_id, len(cuts)

    if minimum_cuts == len(necklace):
        raise ValueError("No fair division found")

    return all_necklace_cuts[minimum_cut_id]


def split_necklace() -> None:
    thieves = 2
    gems_per_thieve = 6
    jewels = thieves * sample(gems_per_thieve * list(Jewel), gems_per_thieve)
    shuffle(jewels)
    necklace = Necklace(jewels)
    print("Initial condition:", necklace)
    print("Solution:", minimum_fair_cuts(necklace, thieves))


if __name__ == "__main__":
    split_necklace()
