"""Advent of code"""

from collections import deque

DIRS = ((-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1))

grid = []

with open('input.txt', 'r', encoding='utf-8') as fin:
    for line in fin:
        grid.append(line.strip())


def get_number_and_mark_visited(grid, r, c, visited):
    """Get the number at the location, and mark starting position as visited."""
    q = deque()

    col = c
    while 0 <= col and grid[r][col].isnumeric():
        q.appendleft(grid[r][col])
        col -= 1

    if (r, col) in visited:
        return 0

    visited.add((r, col))

    col = c + 1
    while col < len(grid[0]) and grid[r][col].isnumeric():
        q.append(grid[r][col])
        col += 1

    return int("".join(q))


def get_sum_of_near_nums(grid, i, j, visited):
    """
    Given a cell position, sum all numbers adjacent to the cell 
    and get summation of them if number has not be visited.

    visited will contain start position of the cell where the number starts.
    """
    total = 0
    for x_delta, y_delta in DIRS:
        if grid[i + x_delta][j + y_delta].isnumeric():
            total += get_number_and_mark_visited(grid, i + x_delta, j + y_delta, visited)

    return total


def get_total(grid):
    """Get total summation of engine parts"""
    total = 0

    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not grid[i][j].isnumeric() and grid[i][j] != '.':  # if special symbol
                total += get_sum_of_near_nums(grid, i, j, visited)

    return total

if __name__ == "__main__":
    print(get_total(grid))
