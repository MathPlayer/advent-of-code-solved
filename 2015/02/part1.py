#!/usr/bin/env python3

filename = 'input'
with open(filename) as f:
    data = f.readlines()

total = 0
for dimensions in data:
    dimensions = dimensions.strip().split('x')
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    surface_area = 2*l*w + 2*w*h + 2*h*l
    slack = min(l*w, w*h, h*l)
    total += surface_area + slack

print(total)
