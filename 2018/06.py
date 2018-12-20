#!/usr/bin/env python3

from collections import Counter


def manhattan(x, y, a, b):
    return abs(x - a) + abs(y - b)


with open("06.in") as f_in:
# with open("06-test.in") as f_in:
    coords = list(map(lambda x: list(map(int, x.strip().split(", "))), f_in.readlines()))

print(coords)
min_x = min(map(lambda x: x[0], coords))
max_x = max(map(lambda x: x[0], coords)) + 1
min_y = min(map(lambda x: x[1], coords))
max_y = max(map(lambda x: x[1], coords)) + 1
print(min_x, max_x, min_y, max_y)

a = [[-1 for _ in range(max_y)] for _ in range(max_x)]

for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        distances = list(map(lambda c: manhattan(c[0], c[1], x, y), coords))
        candidate = min(distances)
        if distances.count(candidate) > 1:
            continue
        a[x][y] = distances.index(candidate)

flat_a = [value for line in a for value in line if value != -1]
print(Counter(flat_a))
print(max(Counter(flat_a).values()))

b = [[0 for _ in range(2000+max_y)] for _ in range(2000+max_x)]
for x in range(2000+max_x):
    print("x = {}".format(x))
    for y in range(2000+max_y):
        distances = sum(map(lambda c: manhattan(c[0] + 1000, c[1] + 1000, x, y), coords))
        if distances < 10000:
            b[x][y] = 1

print(sum(map(sum, b)))
