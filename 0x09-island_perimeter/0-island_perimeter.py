#!/usr/bin/python3
"""
Module defines function island_perimeter.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of island described in grid.
    """
    perimeter = 0
    height = len(grid)
    width = len(grid[0])
    for i in range(height):
        for j in range(width):
            if grid[i][j]:
                free_edges = 4
                # check left
                if j - 1 >= 0 and grid[i][j - 1]:
                    free_edges -= 1
                # check right
                if j + 1 < width and grid[i][j + 1]:
                    free_edges -= 1
                # check above
                if i - 1 >= 0 and grid[i - 1][j]:
                    free_edges -= 1
                # check below
                if i + 1 < height and grid[i + 1][j]:
                    free_edges -= 1
                perimeter += free_edges
    return perimeter
