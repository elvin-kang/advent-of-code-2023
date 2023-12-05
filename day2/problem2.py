"""Advent of code"""

from collections import Counter
from functools import reduce
from typing import Tuple


def process_input(line: str) -> Tuple[int, list[Counter]]:
    """Process Input"""
    game_id, record = line.strip().split(':')
    game_id = int(game_id.split(" ")[-1])

    games = []

    for game in record.split(";"):
        pull = Counter()
        for info in game.split(","):
            num, color = info.strip().split(" ")
            pull[color] += int(num)
        games.append(pull)

    return game_id, games


def get_power(games: list[Counter]) -> int:
    """power: multiplication of min required marbles"""
    counter = Counter()
    for c in games:
        counter |= c

    return reduce(lambda a, b: a * b, counter.values())


with open('input.txt', 'r', encoding='utf-8') as fin:
    total = 0
    for line in fin:
        game_id, games = process_input(line)
        total += get_power(games)
    print(total)
