#!/usr/bin/env python


def read(filename):
    raw = open(filename).readlines()
    ret = []
    for lines in raw:
        direction = lines[0]
        count = int(lines[1:].strip())
        ret.append((direction, count))
    return ret


def solve(filename):
    data = read(filename)

    # Part 1
    pos = 50
    count_of_zero = 0
    for direction, count in data:
        if direction == 'L':
            pos = (pos + 100 - count) % 100
        elif direction == 'R':
            pos = (pos + count) % 100
        if pos == 0:
            count_of_zero += 1

    print(count_of_zero)

    # part 2
    pos = 50
    count_of_zero = 0

    for direction, count in data:
        for _ in range(count):
            if direction == 'L':
                pos = (pos + 100 - 1) % 100
            elif direction == 'R':
                pos = (pos + 1) % 100
            if pos == 0:
                count_of_zero += 1

    print(count_of_zero)


if __name__ == '__main__':
    # solve('test')
    solve('input')
