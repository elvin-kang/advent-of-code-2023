def first_digit(s: str) -> int:
    for char in s:
        if char.isnumeric():
            return char

    raise ValueError("Invalid Input")

def last_digit(s: str) -> int:
    for char in reversed(s):
        if char.isnumeric():
            return char
    
    raise ValueError("Invalid Input")


with open('input.txt', 'r') as fin:
    total = 0

    for line in fin:
        total += int(first_digit(line) + last_digit(line))

    print(total)
