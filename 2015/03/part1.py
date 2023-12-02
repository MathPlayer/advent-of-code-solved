#!/usr/bin/env python3

from collections import defaultdict

filename = 'input'

# Read all data from filename
with open(filename) as f:
    data = f.read().strip()

grid = defaultdict(int)
x = y = 0
grid[(x, y)] = 1
for c in data:
    if c == '^':
        y += 1
    elif c == 'v':
        y -= 1
    elif c == '>':
        x += 1
    elif c == '<':
        x -= 1
    grid[(x, y)] += 1

print(sum(1 for v in grid.values() if v >= 1))
