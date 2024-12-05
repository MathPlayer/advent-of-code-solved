#!/usr/bin/env python3

import re


def read(filename):
    data = open(filename).read().strip()

    return data


def part_1(data):
    result = 0

    matches = re.findall(r'mul\((\d+),(\d+)\)', data)

    for match in matches:
        result += int(match[0]) * int(match[1])

    return result


def part_2(data):
    result = 0

    mul_matches = [(m.groups(), m.start()) for m in re.finditer(r'(mul\((\d+),(\d+)\))', data)]

    do_indices = [m.start() for m in re.finditer(r'do\(\)', data)]
    dont_indices = [m.start() for m in re.finditer(r'don\'t\(\)', data)]

    instruction = None
    for match, index in mul_matches:
        # Could be optimized by using indices on both lists and moving them forward.
        closest_do = [i for i in do_indices if i < index]
        closest_dont = [i for i in dont_indices if i < index]

        if not closest_dont:
            instruction = 'do'
        elif not closest_do:
            instruction = 'dont'
        elif closest_do[-1] > closest_dont[-1]:
            instruction = 'do'
        else:
            instruction = 'dont'

        if instruction != 'dont':
            result += int(match[1]) * int(match[2])

    return result


def solve(filename):
    data = read(filename)

    print("part 1:")
    result = part_1(data)
    print(result)

    print("part 2:")
    result = part_2(data)
    print(result)


if __name__ == '__main__':
    # solve('test')
    solve('input')
