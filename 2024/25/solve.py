#!/usr/bin/env python

def read_input(file_path):
    with open(file_path, 'r') as file:
        raw = file.readlines()

    schematics = {}
    index = 0
    i = 0
    width = len(raw[0].strip())
    height = None
    for line in raw:
        if not line.strip():
            index += 1
            if i != 0:
                height = i
                i = 0
            continue
        for j, char in enumerate(line.strip()):
            if index not in schematics:
                schematics[index] = {}
            schematics[index][(i, j)] = char
        i += 1

    return (width, height), schematics


def get_locks_and_keys(schematics, width, height):
    locks = []
    keys = []
    for schematic in schematics.values():
        top = [schematic[(0, j)] for j in range(width)]
        bottom = [schematic[(height - 1, j)] for j in range(width)]
        if all(c == '#' for c in top) and all(c == '.' for c in bottom):
            locks.append(schematic)
        elif all(c == '.' for c in top) and all(c == '#' for c in bottom):
            keys.append(schematic)
    return locks, keys


def convert_lock_to_heights(lock, width, height):
    heights = []
    for j in range(width):
        col_height = 0
        for i in range(height):
            if lock[(i, j)] == '#':
                col_height += 1
            else:
                break
        heights.append(col_height)
    return heights


def convert_key_to_heights(key, width, height):
    heights = []
    for j in range(width):
        col_height = 0
        for i in range(height - 1, -1, -1):
            if key[(i, j)] == '#':
                col_height += 1
            else:
                break
        heights.append(col_height)
    return heights


def print_schematic(schematic, width, height):
    for i in range(height):
        row = ""
        for j in range(width):
            row += schematic[(i, j)]
        print(row)


def solve(file_path):
    (w, h), schematics = read_input(file_path)

    locks, keys = get_locks_and_keys(schematics, w, h)
    lock_heights = [convert_lock_to_heights(lock, w, h) for lock in locks]
    key_heights = [convert_key_to_heights(key, w, h) for key in keys]

    valid_pairs = 0
    for lock in lock_heights:
        for key in key_heights:
            if any(lock[j] + key[j] > h for j in range(w)):
                continue
            valid_pairs += 1

    print(valid_pairs)


if __name__ == "__main__":
    file = "test"
    solve(file)

    file = "input"
    solve(file)
