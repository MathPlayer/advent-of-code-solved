#!/usr/bin/env python

import sys

# Values taken from https://www.redblobgames.com/grids/hexagons/#neighbors-cube
DIRECTIONS = {
    'e': (1, -1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
    'w': (-1, +1, 0),
    'nw': (0, 1, -1),
    'ne': (1, 0, -1)
}


def read(in_file):
    ''' Reads data for day 24. '''
    paths = []
    with open(in_file) as f:
        for line in tuple(map(lambda x: x.strip(), f.readlines())):
            coord = ''
            path = []
            for c in line:
                if c in ['n', 's']:
                    coord = c
                else:
                    coord = coord + c
                    path.append(coord)
                    coord = ''
            paths.append(tuple(path))
    return paths


def add(x, y):
    ''' Adds two coordinates. '''
    return tuple(map(sum, zip(x, y)))


def flip(paths):
    ''' Returns the black tiles obtained by flipping every tile at the end of each path, starting from (0, 0, 0). '''
    black_tiles = set()
    for path in paths:
        current = (0, 0, 0)
        for coord in path:
            current = add(current, DIRECTIONS[coord])
        if current in black_tiles:
            black_tiles.remove(current)
        else:
            black_tiles.add(current)
    return black_tiles


def conway_hex(black_tiles):
    ''' Returns the black tiles after one round similar to Conway's Game of Life. '''
    new_black_tiles = set()
    neighs = set()

    # Update black tiles.
    for tile in black_tiles:
        count = 0
        for neigh in map(lambda x: add(tile, x), DIRECTIONS.values()):
            if neigh in black_tiles:
                count += 1
            else:
                neighs.add(neigh)
        if 1 <= count <= 2:
            new_black_tiles.add(tile)

    # Update neighbors of black tiles.
    for neigh in neighs:
        count = 0
        for neigh_neigh in map(lambda x: add(neigh, x), DIRECTIONS.values()):
            count += neigh_neigh in black_tiles
        if count == 2:
            new_black_tiles.add(neigh)
    return new_black_tiles


def solve(in_file):
    ''' Solves day 24. '''
    paths = read(in_file)
    print(f"--- {in_file}")

    # Part 1
    black_tiles = flip(paths)
    print(len(black_tiles))

    # Part 2
    for _ in range(100):
        black_tiles = conway_hex(black_tiles)
    print(len(black_tiles))


if __name__ == '__main__':
    solve('24test.in')
    solve('24.in')

    sys.exit(0)
