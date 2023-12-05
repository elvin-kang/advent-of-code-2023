"""Advent of code"""

from collections import Counter


def process_input(line):
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


def possible(games: list[Counter]) -> bool:
    """Check if it's possible to satisfy the games with 12 red, 13 green, 14 blue"""
    for game in games:
        if game.get("red", 0) > 12 or game.get("green", 0) > 13 or game.get("blue", 0) > 14:
            return False

    return True


with open('input.txt', 'r') as fin:
    total = 0
    for line in fin:
        game_id, games = process_input(line)

        if possible(games):
            total += game_id

    print(total)
