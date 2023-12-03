#!/usr/bin/env python3

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
    part_number = False
    result = 0
    for row, line in enumerate(data):
        for col, c in enumerate(line):
            if not c.isdigit():
                if number and part_number:
                    result += int(number)
                number = ''
                part_number = False
                continue

            number += c

            if part_number:
                continue

            for r, c in neighbors(row, col):
                if r < 0 or c < 0 or r >= len(data) or c >= len(data[r]):
                    continue
                if data[r][c] == '.' or data[r][c].isdigit():
                    continue
                part_number = True
                break

    return result


filename = 'input'
# filename = 'test1'

data = open(filename, 'r').readlines()
data = [x.strip() for x in data]
print(solve(data))
