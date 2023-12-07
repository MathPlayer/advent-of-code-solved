#!/usr/bin/env python3


def read_file(filename):
    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]

    for line in data:
        if line.startswith('Time:'):
            times = [int(t) for t in line.split(':')[1].strip().split()]
        if line.startswith('Distance:'):
            distances = [int(t) for t in line.split(':')[1].strip().split()]

    return times, distances


def solve(data):
    times, distances = data
    print(times)
    print(distances)

    ways_count = []
    for i, total_time in enumerate(times):
        way_count = 0
        for hold_time in range(total_time+1):
            travel_time = total_time - hold_time
            distance = hold_time * travel_time
            if distances[i] < distance:
                way_count += 1
        ways_count.append(way_count)

    i = 1
    for x in ways_count:
        i *= x
    print(i)


filename = 'input'
# filename = 'test'
data = read_file(filename)
solve(data)
