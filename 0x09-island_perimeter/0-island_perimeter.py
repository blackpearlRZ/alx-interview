#!/usr/bin/python3
"""This module defines the island_perimeter function
"""


def island_perimeter(grid):
    """This function calculates the perimeter of an island
        defined with a grid.
        Args:
            grid(list): a list of lists containing integers each
            describing the grid cell where 0 means that the
            cell is is a water zone, 1 means it's a land zone.
        Return:
            the perimeter of the island
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                continue
            else:
                if ((i - 1) >= 0) and (grid[i - 1][j] == 0):
                    perimeter += 1
                elif (i - 1) < 0:
                    perimeter += 1
                if (i + 1) < (len(grid)) and (grid[i + 1][j] == 0):
                    perimeter += 1
                elif (i + 1) >= len(grid):
                    perimeter += 1
                if (j + 1) < (len(grid[i])) and (grid[i][j + 1] == 0):
                    perimeter += 1
                elif (j + 1) >= len(grid[i]):
                    perimeter += 1
                if ((j - 1) >= 0) and (grid[i][j - 1] == 0):
                    perimeter += 1
                elif (j - 1) < 0:
                    perimeter += 1
    return perimeter

