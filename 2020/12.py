#!/usr/bin/env python

import sys

NORTH = 'N'
SOUTH = 'S'
WEST = 'W'
EAST = 'E'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'
DIRECTIONS = {
    NORTH: (0, -1),
    EAST: (1, 0),
    SOUTH: (0, 1),
    WEST: (-1, 0)
}
ROTATE_LEFT = {
    NORTH: WEST,
    WEST: SOUTH,
    SOUTH: EAST,
    EAST: NORTH
}
ROTATE_RIGHT = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH
}

def read(in_file):
    ''' Reads data for day 12. '''
    with open(in_file) as f:
        data = tuple(map(lambda x: (x[0], int(x[1:])), f.readlines()))
    return data


def solve_1(data):
    ''' Solves part 1 of day 12. '''
    orientation = EAST
    coords = [0, 0]
    for action, step in data:
        if action == FORWARD:
            coords = (coords[0] + step * DIRECTIONS[orientation][0], coords[1] + step * DIRECTIONS[orientation][1])
        elif action in DIRECTIONS:
            coords = (coords[0] + step * DIRECTIONS[action][0], coords[1] + step * DIRECTIONS[action][1])
        elif action == LEFT:
            # Assume only multiples of 90.
            for _ in range(step // 90):
                orientation = ROTATE_LEFT[orientation]
        elif action == RIGHT:
            # Assume only multiples of 90.
            for _ in range(step // 90):
                orientation = ROTATE_RIGHT[orientation]
    print(abs(coords[0]) + abs(coords[1]))


def solve_2(data):
    ''' Solves part 2 of day 12. '''
    coords = [0, 0]
    waypoint = [10, -1]
    for action, step in data:
        if action == FORWARD:
            coords = (coords[0] + step * waypoint[0], coords[1] + step * waypoint[1])
        elif action in DIRECTIONS:
            waypoint = (waypoint[0] + step * DIRECTIONS[action][0], waypoint[1] + step * DIRECTIONS[action][1])
        elif action == LEFT:
            # Assume only multiples of 90.
            for _ in range(step // 90):
                waypoint = (waypoint[1], -waypoint[0])
        elif action == RIGHT:
            # Assume only multiples of 90.
            for _ in range(step // 90):
                waypoint = (-waypoint[1], waypoint[0])
    print(abs(coords[0]) + abs(coords[1]))


def solve(in_file):
    ''' Solves day 12. '''
    print(in_file)
    data = read(in_file)
    solve_1(data)
    solve_2(data)


if __name__ == '__main__':
    solve('12test.in')
    solve('12.in')

    sys.exit(0)
