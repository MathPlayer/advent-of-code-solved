#!/usr/bin/env python3

from collections import defaultdict

def solve(data):

    def neighbors(row, col):
        yield row, col + 1
        yield row, col - 1
        yield row + 1, col
        yield row - 1, col
        yield row - 1, col - 1
        yield row - 1, col + 1
        yield row + 1, col - 1
        yield row + 1, col + 1

    number = ''
    gear_number = False
    gear = (-1, -1)

    gears = defaultdict(list)
    for row, line in enumerate(data):
        for col, c in enumerate(line):
            if not c.isdigit():
                if number and gear_number:
                    gears[gear].append(int(number))
                gear = (-1, -1)
                number = ''
                gear_number = False
                continue

            number += c

            if gear_number:
                continue

            for r, c in neighbors(row, col):
                if r < 0 or c < 0 or r >= len(data) or c >= len(data[r]):
                    continue
                if data[r][c] == '.' or data[r][c].isdigit():
                    continue
                gear_number = True
                gear = (r, c)
                break

    result = 0
    for gear, numbers in gears.items():
        if len(numbers) != 2:
            continue
        result += numbers[0] * numbers[1]
    return result


filename = 'input'
# filename = 'test1'

data = open(filename, 'r').readlines()
data = [x.strip() for x in data]
print(solve(data))
