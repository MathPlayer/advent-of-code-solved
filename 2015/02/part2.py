#!/usr/bin/env python3

filename = 'input'
with open(filename) as f:
    data = f.readlines()

total = 0
for dimensions in data:
    dimensions = dimensions.strip().split('x')
    x = int(dimensions[0])
    y = int(dimensions[1])
    z = int(dimensions[2])
    total += x * y * z + 2 * (x + y + z - max(x, y, z))

print(total)
