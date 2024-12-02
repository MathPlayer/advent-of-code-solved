#!/usr/bin/env python3


def read(filename):
    data = open(filename).readlines()
    data = [x.strip() for x in data]

    data = [list(map(int, x.split())) for x in data]

    return data


def part_1(data):
    result = 0

    for line in data:
        if all([line[i] - line[i - 1] in [1, 2, 3] for i in range(1, len(line))]):
            result += 1
        elif all([line[i] - line[i - 1] in [-1, -2, -3] for i in range(1, len(line))]):
            result += 1

    print(result)


def part_2(data):
    result = 0

    for line in data:
        found = False
        for i in range(len(line)):
            line_without_i = line[:i] + line[i + 1:]
            if all([line_without_i[j] - line_without_i[j - 1] in [1, 2, 3] for j in range(1, len(line_without_i))]):
                found = True
                break
            elif all([line_without_i[j] - line_without_i[j - 1] in [-1, -2, -3] for j in range(1, len(line_without_i))]):
                found = True
                break
        if found:
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
