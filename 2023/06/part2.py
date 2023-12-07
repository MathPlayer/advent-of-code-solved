#!/usr/bin/env python3


def read_file(filename):
    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]

    for line in data:
        if line.startswith('Time:'):
            time = int(line.split(':')[1].strip().replace(' ', ''))
        if line.startswith('Distance:'):
            distance = int(line.split(':')[1].strip().replace(' ', ''))

    return time, distance


def solve(data):
    time, distance = data

    first = 0
    last = time+1
    for hold_time in range(time+1):
        travel_time = time - hold_time
        way_distance = hold_time * travel_time
        if distance < way_distance:
            first = hold_time
            break

    for hold_time in range(time+1, 0, -1):
        travel_time = time - hold_time
        way_distance = hold_time * travel_time
        if distance < way_distance:
            last = hold_time
            break

    print(last - first + 1)


filename = 'input'
# filename = 'test'
data = read_file(filename)
solve(data)
