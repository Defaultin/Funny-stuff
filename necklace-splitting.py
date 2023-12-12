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


def split_necklace(necklace: list[str]) -> list[list[str]]:
    pass


if __name__ == "__main__":
    t1 = ["S", "E", "S", "E", "S", "D", "S", "D", "D", "E", "E", "D"]
    r1 = [["S", "E", "S"], ["E", "S", "D", "S"], ["D", "D", "E"], ["E", "D"]]
    t2 = ["S", "S", "S", "S", "E", "E", "D", "D", "D", "D", "D", "D"]
    r2 = [["S", "S"], ["S", "S", "E"], ["E", "D", "D", "D"], ["D", "D", "D"]]
    t3 = ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S"]
    r3 = [["S", "S", "S", "S", "S", "S"], ["S", "S", "S", "S", "S", "S"]]
    t4 = ["S", "S", "S", "S", "E", "D", "R", "E", "D", "R", "E", "E"]
    r4 = [["S", "S"], ["S", "S", "E", "D", "R", "E"], ["D", "R", "E", "E"]]

    assert split_necklace(t1) == r1
    assert split_necklace(t2) == r2
    assert split_necklace(t3) == r3
    assert split_necklace(t4) == r4
