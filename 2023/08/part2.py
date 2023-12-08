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


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(numbers):
    lcm = numbers[0]
    for i in numbers[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


def solve(data):
    instructions, tree = data
    start_nodes = [node for node in tree if node.endswith('A')]
    steps = []
    for node in start_nodes:
        i = 0
        step = 0
        while not node.endswith('Z'):
            step += 1
            if instructions[i] == 'L':
                node = tree[node][0]
            else:
                node = tree[node][1]
            i = (i + 1) % len(instructions)
        steps.append(step)

    print(lcm(steps))


filename = 'input'
# filename = 'test'
# filename = 'test2'
# filename = 'test3'

data = read_lines(filename)
solve(data)
