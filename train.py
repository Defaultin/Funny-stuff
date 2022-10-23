import numpy as np


class Train(list):
    """
    In a dark sandstorm, a train with completely identical carriages
    travels along rails closed in a circle,
    the last carriage of which is fastened to the first
    so that inside you can move freely between the carriages.

    You ended up in one random carriage and your task is to count their total number.
    In each carriage, you can turn the lights on (state=1) or off (state=0),
    but the initial position of the switches is random and is not known in advance.
    
    Note: The number of carriages is finite and you cannot mark them
    in any way other than turning the lights on or off.
    """
    def __init__(self, size, states=[0,1]):
        self._size = size
        self._train = np.random.choice(states, size=(size,)).tolist()
        super().__init__(self._train)

    def __getitem__(self, idx):
        return self._train[idx]

    def __setitem__(self, idx, value):
        self._train[idx % self._size] = value

    def __iter__(self):
        self._idx = 0
        return self

    def __next__(self):
        self._idx += 1
        if self._idx <= self._size:
            return self._train[self._idx - 1]
        else:
            self._idx = 0
            return self._train[0]

    def __repr__(self):
        size = self._size // 2 if self._size < 10 else 10
        return f"[{', '.join(str(c) for c in self._train[:size])} ...]"


def solution(train):
    train[0] = guess = 1
    while train[0]:
        for idx, carriage in enumerate(train):
            if carriage and idx > 0:
                train[idx] = 0
                guess = idx
                break
    return guess


def main():
    size = np.random.randint(999, 9999)
    train = Train(size)
    result = solution(train)
    print(f"Guess: {result}\nCorrect: {result == size}")


if __name__ == "__main__":
    main()
