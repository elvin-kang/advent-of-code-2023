"""Advent of code"""

from collections import deque

DIRS = ((-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1))


def get_number_at(grid, r, c, visited):
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


def get_sum_of_gear_ratios(grid, i, j):
    """
    Given a cell position, sum all numbers adjacent to the cell 
    and get summation of them if number has not be visited.

    visited will contain start position of the cell where the number starts.
    """
    nums = []

    visited = set()

    for x_delta, y_delta in DIRS:
        if grid[i + x_delta][j + y_delta].isnumeric():
            number = get_number_at(grid, i + x_delta, j + y_delta, visited)
            if number > 0:
                nums.append(number)

    if len(nums) == 2:
        return nums[0] * nums[1]

    return 0


def get_total_gear_ratio(grid):
    """Get total summation of engine parts"""
    total = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '*':
                total += get_sum_of_gear_ratios(grid, i, j)

    return total


grid = []

with open('input.txt', 'r', encoding='utf-8') as fin:
    for line in fin:
        grid.append(line.strip())

print(get_total_gear_ratio(grid))
