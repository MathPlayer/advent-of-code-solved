#!/usr/bin/env python3

from collections import defaultdict

filename = 'input'

# Read all data from filename
with open(filename) as f:
    data = f.read().strip()

grid = defaultdict(int)
x = y = 0
a = b = 0
grid[(x, y)] = 1
turn = 'santa'
for c in data:
    change = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}[c]
    if turn == 'santa':
        x += change[0]
        y += change[1]
        grid[(x, y)] += 1
        turn = 'robot'
    elif turn == 'robot':
        a += change[0]
        b += change[1]
        grid[(a, b)] += 1
        turn = 'santa'

print(sum(1 for v in grid.values() if v >= 1))
