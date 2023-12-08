#!/usr/bin/env python3


def read_lines(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    instructions = ''
    tree = {}
    for line in lines:
        if not line:
            continue
        if '=' not in line:
            instructions = line
            continue
        root, rest = line.strip(')').split(' = (')
        left, right = rest.split(', ')
        tree[root] = (left, right)

    return instructions, tree


def solve(data):
    instructions, tree = data
    current = 'AAA'
    i = 0
    path = []
    while current != 'ZZZ':
        if len(path) % 100 == 0:
            print(len(path))
        path.append(current)
        if instructions[i] == 'L':
            current = tree[current][0]
        else:
            current = tree[current][1]
        i = (i + 1) % len(instructions)
    print(len(path))


filename = 'input'
# filename = 'test'
# filename = 'test2'

data = read_lines(filename)
solve(data)
