import numpy as np


class Sudoku:
    '''
    Sudoku generator and solver.

    Arguments
    ---------
    grid : array_like, optional
        Unsolved sudoku 9x9 grid. If None (default), 
        generates random sudoku grid.
    difficulty : int, optional
        The complexity parameter of the generated 
        sudoku grid (from 1 to 5, 3 by default).

    '''
    def __init__(self, grid=None, *, difficulty=3):
        if 0 < difficulty < 6 and isinstance(difficulty, int):
            self.difficulty = difficulty
        else:
            raise ValueError('Difficulty index must be between 1 and 5!')
        if grid is not None:
            self.grid = self.set_grid(grid)
        else:
            self.grid = self.get_grid()

        self._template = [
            '╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗',
            '║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║',
            '╟───┼───┼───╫───┼───┼───╫───┼───┼───╢',
            '╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣',
            '╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝'
        ]


    def set_grid(self, grid):
        '''
        Sets a sudoku grid.

        Parameters
        ----------
        grid : array_like
            Unsolved sudoku grid (shape 9x9).
        '''
        if grid.shape != (9, 9):
            raise ValueError('Expected 9x9 sudoku grid!')
        else:
            self.grid = np.array(grid, dtype=np.int8)   


    def get_grid(self):
        '''
        Generates a random sudoku grid.

        Returns
        -------
        out : numpy.ndarray
            Random unsolved sudoku grid (shape 9x9).
        '''
        valid = lambda r, c: (3 * (r % 3) + r // 3 + c) % 9
        shuffle = lambda n: np.random.choice(n, size=len(n), replace=False)
        rng = range(3)
        nums = shuffle(range(1, 10))
        rows = [3 * i + r for i in shuffle(rng) for r in shuffle(rng)] 
        cols = [3 * i + c for i in shuffle(rng) for c in shuffle(rng)]
        self.grid = np.array([[nums[valid(r, c)] for c in cols] for r in rows], dtype=np.int8)

        for i in np.random.choice(range(81), size=13 * self.difficulty, replace=False):
            self.grid[divmod(i, 9)] = 0

        return self.grid


    def print_grid(self):
        '''Renders sudoku grid.'''
        print(self._template[0])
        for i in range(9):
            num_str = zip([''] + self.grid[i].tolist(), self._template[1].split('.'))
            idx = ((i + 1) % 9 == 0) + ((i + 1) % 3 == 0)
            print(''.join(str(n) + s if n != 0 else ' ' + s for n, s in num_str))
            print(self._template[idx+2])


    def solve(self, n=0):
        '''
        Solves sudoku grid.

        Parameters
        ----------
        n : int, optional
            Flattened sudoku grid index (0 by default).
        
        Returns
        -------
        out : numpy.ndarray
            Solved sudoku grid (shape 9x9).
        '''
        if n >= 81:
            return self.grid
        if self.grid.flatten()[n]:
            return self.solve(n + 1)

        # (row, col) for grid
        i, j = n // 9, n % 9

        # (row, col) for box
        k, l = i // 3, j // 3

        # possible numbers
        guesses = set(range(1, 10)) - (
            set(self.grid[i]) |
            set(self.grid.T[j]) |
            set(self.grid[3*k:3*k+3, 3*l:3*l+3].flatten())
        )

        # grid backtracking
        for guess in guesses:
            self.grid[i, j] = guess
            if self.solve(n + 1) is not None:
                return self.grid
        else:
            self.grid[i, j] = 0



if __name__ == '__main__':
    sudoku = Sudoku(difficulty=4)
    sudoku.print_grid()
    sudoku.solve()
    sudoku.print_grid()
