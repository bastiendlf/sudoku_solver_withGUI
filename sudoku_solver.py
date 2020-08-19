# -*- coding: utf-8 -*-
import time

grids = list()

grids.append([
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
])

grids.append([
    [0, 0, 5, 0, 0, 0, 1, 0, 0],
    [0, 6, 1, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 3, 8, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 3, 0, 0, 0, 9],
    [0, 1, 3, 5, 0, 0, 0, 0, 2],
    [9, 0, 0, 0, 0, 2, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [4, 0, 0, 0, 5, 9, 0, 0, 3]
]
)

grid = grids[0]

# grid[row][col]

"""# **Function to print a sudoku grid**"""


def print_grid(grid: list):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('- - - + - - - + - - -')
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('| ', end='')

            if j != 8:
                print(str(grid[i][j]) + ' ', end='')
            else:
                print(str(grid[i][j]))


"""# **Check if a number can fit in a cell**"""


def possible(grid: list, row: int, col: int, number: int):
    # check in column if possible to place number
    for i in range(9):
        if grid[row][i] == number and col != i:
            return False

    # chek in line if possible to place number
    for j in range(9):
        if grid[j][col] == number and row != j:
            return False

    # check in the square if possible to place number

    row0 = (row // 3) * 3
    col0 = (col // 3) * 3

    for i in range(row0, row0 + 3):
        for j in range(col0, col0 + 3):
            if grid[i][j] == number and (i, j) != (row, col):
                return False
    return True


"""# **Find first empty cell**"""


def find_empty(grid: list):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # row, col


"""# **Solve the Sudoku**"""


def solve(grid: list):
    time.sleep(0.05)
    find_row_col = find_empty(grid)

    if not find_row_col:
        return True
    else:
        row, col = find_row_col

    for n in range(1, 10):
        if possible(grid, row, col, n):

            grid[row][col] = n

            if solve(grid):
                return True

            grid[row][col] = 0

    return False


if __name__ == "__main__":
    print("Sudoku:")
    print_grid(grid)
    solve(grid)
    print("Solved:")
    print_grid(grid)
