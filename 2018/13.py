#!/usr/bin/env python3

VERTICAL = "|"
HORIZONTAL = "-"
CROSS = "+"
CRASH = "X"
SLASH = "/"
BACKSLASH = "\\"

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

TURN = {
    VERTICAL: {UP: UP, DOWN: DOWN},
    HORIZONTAL: {LEFT: LEFT, RIGHT: RIGHT},
    SLASH: {UP: RIGHT, RIGHT: UP, DOWN: LEFT, LEFT: DOWN},
    BACKSLASH: {UP: LEFT, LEFT: UP, DOWN: RIGHT, RIGHT: DOWN},
    CROSS: {
        0: {UP: LEFT, LEFT: DOWN, DOWN: RIGHT, RIGHT: UP},
        1: {UP: UP, LEFT: LEFT, DOWN: DOWN, RIGHT: RIGHT},
        2: {UP: RIGHT, LEFT: UP, DOWN: LEFT, RIGHT: DOWN}
    }
}

PRINT_DIRECTION = {
    UP: "^",
    LEFT: "<",
    RIGHT: ">",
    DOWN: "v"
}


def read(filename):
    with open(filename) as f:
        lines = list(map(lambda x: list(x.strip("\n")), f))
    return lines


def extract_carts(grid):
    carts = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "^":
                carts.append(((y, x), UP, 0))
                grid[y][x] = VERTICAL
            if grid[y][x] == "v":
                carts.append(((y, x), DOWN, 0))
                grid[y][x] = VERTICAL
            if grid[y][x] == ">":
                carts.append(((y, x), RIGHT, 0))
                grid[y][x] = HORIZONTAL
            if grid[y][x] == "<":
                carts.append(((y, x), LEFT, 0))
                grid[y][x] = HORIZONTAL
    return (grid, carts)


def move_carts(grid, carts):
    new_carts = []
    crash = None
    removed = []
    for i in range(len(carts)):
        # Ignore crashed/removed carts
        if not carts[i][0]:
            continue

        position, direction, cross_option = carts[i]

        # Move
        new_position = tuple(map(sum, zip(position, direction)))

        # Crash
        if new_position in map(lambda x: x[0], carts):
            print("crash: {},{}".format(new_position[1], new_position[0]))
            carts = list(map(
                lambda x: (None, None, None) if x[0] in [position, new_position] else x, carts))
            continue

        # Direction change
        g = grid[new_position[0]][new_position[1]]
        if g == SLASH:
            direction = TURN[SLASH][direction]
        elif g == BACKSLASH:
            direction = TURN[BACKSLASH][direction]
        elif g == CROSS:
            direction = TURN[CROSS][cross_option][direction]
            cross_option = (cross_option + 1) % 3

        carts[i] = (new_position, direction, cross_option)

    return sorted(filter(lambda x: x[0] is not None, carts))


def print_grid_carts(grid, carts):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            sign = grid[y][x]
            for position, direction, _ in carts:
                if position == (y, x):
                    sign = PRINT_DIRECTION[direction]
                    break
            print(sign, end="", sep="")
        print()


def solve():
    filename = "13.in"
    # filename = "13test.in"
    grid, carts = extract_carts(read(filename))
    # print_grid_carts(grid, carts)

    carts_count = len(carts)
    crash = None
    while len(carts) >= 2:
        carts = move_carts(grid, carts)
        # print_grid_carts(grid, carts)
    print("cart: {},{}".format(carts[0][0][1], carts[0][0][0]))


solve()
