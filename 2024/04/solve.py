#!/usr/bin/env python3


DIRECTIONS = {
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
}


def read(filename):
    data = open(filename).readlines()
    data = [x.strip() for x in data]

    return data


def part_1(data):
    result = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            for direction in DIRECTIONS:
                x, y = i, j
                word = ''
                while 0 <= x < len(data) and 0 <= y < len(data[0]):
                    word += data[x][y]
                    if word == 'XMAS':
                        result += 1
                        break
                    x += direction[0]
                    y += direction[1]

    print(result)


def part_2(data):
    result = 0

    patterns = [
        ''.join(['M.S', '.A.', 'M.S']),
        ''.join(['M.M', '.A.', 'S.S']),
        ''.join(['S.M', '.A.', 'S.M']),
        ''.join(['S.S', '.A.', 'M.M']),
    ]

    # Form all 3x3 blocks from the matrix of characters, and check if any of the patterns match.
    for i in range(len(data) - 2):
        for j in range(len(data[0]) - 2):
            block = ''.join([data[i + k][j:j + 3] for k in range(3)])
            if len(block) != 9:
                continue
            for pattern in patterns:
                if all([block[k] == pattern[k] or pattern[k] == '.' for k in range(9)]):
                    result += 1

    print(result)


def solve(filename):
    data = read(filename)

    print("part 1:")
    part_1(data)

    print("part 2:")
    part_2(data)


if __name__ == '__main__':
    # solve('test')
    solve('input')
