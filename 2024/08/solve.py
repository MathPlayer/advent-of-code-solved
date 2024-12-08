#!/usr/bin/env python3


def read(filename):
    data = open(filename).readlines()
    data = [x.strip() for x in data]

    result = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            result[(i, j)] = char

    return result


def get_antennas_lists(data):
    antennas = {}
    for pos, value in data.items():
        if value == '.':
            continue
        if value not in antennas:
            antennas[value] = []
        antennas[value].append(pos)

    # Sort the antennas list by value.
    return {x: sorted(y) for x, y in antennas.items()}


def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1])


def print_grid(data):
    print("------------------------------------------------")
    max_x = max(x for x, _ in data.keys())
    max_y = max(y for _, y in data.keys())

    for i in range(max_x + 1):
        for j in range(max_y + 1):
            print(data[(i, j)], end='')
        print()


def part_1(data):
    result = set()
    # print_grid(data)

    antennas = get_antennas_lists(data)

    for value, positions in antennas.items():
        # iterate through each pair of antennas from the same value.
        for i, pos1 in enumerate(positions):
            for j, pos2 in enumerate(positions):
                if i >= j:
                    continue
                # print(f"--- Antennas {pos1} and {pos2}")
                d_a_x, d_a_y = distance(pos1, pos2)
                possible_antinodes = []
                if d_a_x == 0:
                    # same row.
                    possible_antinodes.append((pos1[0], pos1[1] - d_a_y))
                    possible_antinodes.append((pos1[0], pos2[1] + d_a_y))
                elif d_a_y == 0:
                    # same column.
                    possible_antinodes.append((pos1[0] - d_a_x, pos1[1]))
                    possible_antinodes.append((pos2[0] + d_a_x, pos1[1]))
                elif pos1[0] < pos2[0] and pos1[1] < pos2[1]:
                    # diagonal from top-left to bottom-right.
                    possible_antinodes.append((pos1[0] - d_a_x, pos1[1] - d_a_y))
                    possible_antinodes.append((pos2[0] + d_a_x, pos2[1] + d_a_y))
                elif pos1[0] < pos2[0] and pos1[1] > pos2[1]:
                    # diagonal from bottom-left to top-right.
                    possible_antinodes.append((pos1[0] - d_a_x, pos1[1] + d_a_y))
                    possible_antinodes.append((pos2[0] + d_a_x, pos2[1] - d_a_y))

                # print(f"Possible antinodes: {possible_antinodes}")
                for possible_antinode in possible_antinodes:
                    if possible_antinode not in data:
                        continue
                    d1 = sum(distance(pos1, possible_antinode))
                    d2 = sum(distance(pos2, possible_antinode))
                    # print(f"Distances: {d1}, {d2}")
                    if d1 == 2 * d2 or d2 == 2 * d1:
                        # if data[possible_antinode] == '.':
                        #     data[possible_antinode] = '#'
                        result.add(possible_antinode)

    # print_grid(data)
    
    return len(result)


def part_2(data):
    result = set()
    # print_grid(data)

    antennas = get_antennas_lists(data)

    for value, positions in antennas.items():
        for i, pos1 in enumerate(positions):
            for j, pos2 in enumerate(positions):
                if i >= j:
                    continue
                # print(f"--- Antennas {pos1} and {pos2}")

                d_a_x, d_a_y = distance(pos1, pos2)

                possible_antinodes = [pos1, pos2]
                # Go left from pos1 until getting out of grid in increments of d_a_x, d_a_y.
                if pos1[1] <= pos2[1]:
                    antinode = pos1
                    while True:
                        antinode = (antinode[0] - d_a_x, antinode[1] - d_a_y)
                        if antinode in data:
                            possible_antinodes.append(antinode)
                        else:
                            break
                else:
                    antinode = pos1
                    while True:
                        antinode = (antinode[0] - d_a_x, antinode[1] + d_a_y)
                        if antinode in data:
                            possible_antinodes.append(antinode)
                        else:
                            break

                # Go right from pos2 until getting out of grid in increments of d_a_x, d_a_y.
                if pos1[1] <= pos2[1]:
                    antinode = pos2
                    while True:
                        antinode = (antinode[0] + d_a_x, antinode[1] + d_a_y)
                        if antinode in data:
                            possible_antinodes.append(antinode)
                        else:
                            break
                else:
                    antinode = pos2
                    while True:
                        antinode = (antinode[0] + d_a_x, antinode[1] - d_a_y)
                        if antinode in data:
                            possible_antinodes.append(antinode)
                        else:
                            break

                # print(f"Possible antinodes: {possible_antinodes}")
                for possible_antinode in possible_antinodes:
                    if possible_antinode not in data:
                        continue
                    # if data[possible_antinode] == '.':
                    #     data[possible_antinode] = '#'
                    result.add(possible_antinode)
    
    return len(result)


def solve(filename):
    data = read(filename)

    print("part 1:")
    result = part_1(data)
    print(result)

    print("part 2:")
    result = part_2(data)
    print(result)


if __name__ == '__main__':
    # solve(f'test')
    # solve(f'test2')
    solve('input')