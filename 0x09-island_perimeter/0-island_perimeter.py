#!/usr/bin/python3
"""
A script for calculating perimeter of an island represented in a 2d grid
"""


def island_perimeter(grid):
    """calculat the perimeter of the island described in a grid

    Args:
        grid (list of list(int)): 2d matrix where 0 reperesent water, and 1
        reperesent island.
            - each cell is square, with side of length 1.
            - grid is rectangular, with its width and height not exceeding 100
            - The grid is completely surrounded by water
            - There is only one island (or nothing).
            - The island doesn't have “lakes” (water inside that isn't
              connected to the water surrounding the island).
    Return:
        - perimeter of the island
    """
    w = len(grid)
    if w <= 1:
        return 0
    h = len(grid[0])
    p = 0
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            if grid[i][j] == 1:
                p += (grid[i + 1][j] == 0) + (grid[i - 1][j] == 0)
                p += (grid[i][j + 1] == 0) + (grid[i][j - 1] == 0)

    return p
