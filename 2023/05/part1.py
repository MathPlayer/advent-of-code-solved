#!/usr/bin/env python3


def read_data(filename):

    with open(filename) as f:
        raw = [line.strip() for line in f.readlines()]

    data = {}
    seeds = []
    mode = ''
    for line in raw:
        if not line:
            mode = ''
            continue
        print(line)
        if line.startswith('seeds'):
            seeds = line.split(':')[-1].strip().split(' ')
            seeds = [int(s) for s in seeds]
            continue
        if line.startswith('seed-to-soil'):
            mode = 'seed-to-soil'
            continue
        if line.startswith('soil-to-fertilizer'):
            mode = 'soil-to-fertilizer'
            continue
        if line.startswith('fertilizer-to-water'):
            mode = 'fertilizer-to-water'
            continue
        if line.startswith('water-to-light'):
            mode = 'water-to-light'
            continue
        if line.startswith('light-to-temperature'):
            mode = 'light-to-temperature'
            continue
        if line.startswith('temperature-to-humidity'):
            mode = 'temperature-to-humidity'
            continue
        if line.startswith('humidity-to-location'):
            mode = 'humidity-to-location'
            continue

        if mode:
            numbers = [int(x) for x in line.split()]
            if mode not in data:
                data[mode] = [numbers]
            else:
                data[mode].append(numbers)

    return seeds, data


def a_t_b(data, val):
    for destination, source, i in data:
        if val >= source and val < source + i:
            return destination + val - source

    return val


def solve(data):
    keys = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    seeds, maps = data
    result = None
    for seed in seeds:
        val = [seed]
        for key, next_key in zip(keys, keys[1:]):
            val.append(a_t_b(maps[f'{key}-to-{next_key}'], val[-1]))
        print(seed, val)
        if not result:
            result = val[-1]
        else:
            result = min(result, val[-1])

    print(result)


filename = 'input'
# filename = 'test'

data = read_data(filename)
solve(data)
