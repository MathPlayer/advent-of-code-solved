# filename = 'input-test.txt'
filename = 'input.txt'
data = [line.strip().split() for line in open(filename, 'r').readlines()]

horizontal = 0
depth = 0
for direction, units in data:
    if direction == 'forward':
        horizontal += int(units)
    if direction == 'down':
        depth += int(units)
    if direction == 'up':
        depth -= int(units)

print(horizontal * depth)
