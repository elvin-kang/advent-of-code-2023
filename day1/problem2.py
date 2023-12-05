"""Day1"""

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def spell_to_str_digit(spell):
    """one -> 1"""
    return str(digits.index(spell) + 1)


def get_numeric_digit(s, first=True):
    """"""
    if not first:
        length = len(s)
        s = reversed(s)

    for i, char in enumerate(s):
        if char.isdigit():
            if not first:
                i = length - i - 1
            return char, i

    return None, None


def first_digit(s: str) -> int:
    indices = {digit: s.find(digit) for digit in digits if s.find(digit) > -1}

    if indices:
        min_key = min(indices, key=indices.get)

        digit, index = get_numeric_digit(s, first=True)

        if digit is None or indices[min_key] < index:
            return spell_to_str_digit(min_key)

        return digit
    else:
        digit, index = get_numeric_digit(s, first=True)
        return digit


def last_digit(s: str) -> int:
    indices = {digit: s.rfind(digit) for digit in digits if s.rfind(digit) > -1}
    if indices:
        max_key = max(indices, key=indices.get)
        digit, index = get_numeric_digit(s, first=False)

        if index is None or indices[max_key] > index:
            return spell_to_str_digit(max_key)

        return digit
    else:
        digit, index = get_numeric_digit(s, first=False)
        return digit


with open('input.txt', 'r') as fin:
    total = 0
    for line in fin:
        total += int(first_digit(line) + last_digit(line))
    print(total)
