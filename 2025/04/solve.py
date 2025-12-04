#!/usr/bin/env python


def read_input(file_path):
    with open(file_path, 'r') as file:
        raw = file.read()

    parsed = {}
    for i, line in enumerate(raw.splitlines()):
        for j, char in enumerate(line):
            parsed[(i, j)] = char

    return parsed


def count_adjacent_at_symbols(data, i, j):
    adjacent_count = 0
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for di, dj in offsets:
        ni, nj = i + di, j + dj
        if (ni, nj) in data and data[(ni, nj)] == '@':
            adjacent_count += 1

    return adjacent_count


def get_positions(data):
    result = []
    for (i, j), value in data.items():
        if count_adjacent_at_symbols(data, i, j) < 4 and data[(i, j)] == '@':
            result.append((i, j))

    return result


def solve(file_path):
    data = read_input(file_path)
    print("part 1")
    result = get_positions(data)
    print(len(result))

    print("part 2")
    round_count = 0
    result = 0
    while any(True for v in data.values() if v == '@'):
        # print(f"Round {round_count}")
        positions = get_positions(data)
        if not positions:
            break
        result += len(positions)
        for pos in positions:
            data[pos] = '.'
        round_count += 1

    print(result)


if __name__ == "__main__":
    file = "test"
    solve(file)

    file = "input"
    solve(file)
