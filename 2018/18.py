#!/usr/bin/env python3

PAD = ' '
OPEN = '.'
TREE = '|'
YARD = '#'


def read_data(filename):
    with open(filename) as f:
        lines = list(map(lambda x: [PAD] + list(x.strip()) + [PAD], f.readlines()))
    return [[PAD] * len(lines[0])] + lines + [[PAD] * len(lines[0])]


def print_area(area):
    for y in range(len(area)):
        for x in range(len(area[0])):
            print(area[y][x], end="", sep="")
        print()


def change(area):
    new_area = [[PAD for _ in range(len(area[0]))] for _ in range(len(area))]
    for y in range(1 ,len(area) - 1):
        for x in range(1, len(area[0]) - 1):
            tree_n = 0
            yard_n = 0
            open_n = 0
            for j in range(-1, 2):
                for i in range(-1, 2):
                    if not i and not j:
                        continue
                    if area[y + j][x + i] == TREE:
                        tree_n += 1
                    elif area[y + j][x + i] == YARD:
                        yard_n += 1
                    elif area[y + j][x + i] == OPEN:
                        open_n += 1
            if area[y][x] == OPEN and tree_n >= 3:
                new_area[y][x] = TREE
            elif area[y][x] == TREE and yard_n >= 3:
                new_area[y][x] = YARD
            elif area[y][x] == YARD and (tree_n < 1 or yard_n < 1):
                new_area[y][x] = OPEN
            else:
                new_area[y][x] = area[y][x]

    return new_area


def value(area):
    tree_n = 0
    yard_n = 0
    for y in range(1, len(area) - 1):
        for x in range(1, len(area[0]) - 1):
            if area[y][x] == TREE:
                tree_n += 1
            elif area[y][x] == YARD:
                yard_n += 1
    return tree_n * yard_n


area = read_data("18test.in")
area = read_data("18.in")
saved = set()
cycle_len = 0
initial = 0
scores = {}
for i in range(1, 1000000000):
    print(i)
    area = change(area)
    line = "".join(map(lambda x: "".join(x), area))
    if line in saved:
        if not initial:
            initial = i
            print("start cycle at {}".format(i))
            saved = set()
        else:
            cycle_len = i - initial
            print("Repeat at {}".format(i))
            break
    saved.add(line)
    scores[i] = value(area)

print(scores[9])
# Hate this formula.
print(scores[initial + (1000000000 - initial) % cycle_len])
