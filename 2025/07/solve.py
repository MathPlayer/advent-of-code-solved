#!/usr/bin/env python

def read_input(file_path):
    with open(file_path, 'r') as file:
        raw = file.read()

    parsed = {}
    for i, line in enumerate(raw.splitlines()):
        for j, char in enumerate(line):
            parsed[(i, j)] = char

    return parsed


def print_data(data):
    for k in sorted(data.keys()):
        i, j = k
        if j == 0:
            print()
        print(data[k], end='')
    print("\n------------------------------------")


def part_1(data):
    tachions = [(i, j) for (i, j), v in data.items() if v == 'S']
    visited = set()
    answer = 0
    while tachions:
        i, j = tachions.pop()
        while True:
            if (i, j) not in data or (i, j) in visited:
                break

            visited.add((i, j))
            cell = data[(i, j)]
            if cell == '^':
                answer += 1
                left = (i, j - 1)
                right = (i, j + 1)
                if left in data and left not in visited:
                    tachions.append(left)
                if right in data and right not in visited:
                    tachions.append(right)
                break

            if cell == '.':
                data[cell] = '|'

            i += 1
    print(answer)


def part_2(data):
    rows = max(i for (i, j) in data.keys()) + 1
    cols = max(j for (i, j) in data.keys()) + 1

    start = next((i, j) for (i, j), v in data.items() if v == 'S')

    timelines = [0] * cols
    timelines[start[1]] = 1

    for i in range(rows):
        new_timelines = [0] * cols
        for j in range(cols):
            if (i, j) not in data:
                continue

            count = timelines[j]
            if count == 0:
                continue

            if data[(i, j)] == '^':
                if j - 1 >= 0:
                    new_timelines[j - 1] += count
                if j + 1 < cols:
                    new_timelines[j + 1] += count
            else:
                new_timelines[j] += count

        timelines = new_timelines

    print(sum(timelines))


def solve(file_path):
    print(f">>>> {file_path}")
    data = read_input(file_path)
    print("part 1")
    part_1(data.copy())

    print("part 2")
    part_2(data)


if __name__ == "__main__":
    file = "test"
    solve(file)

    file = "input"
    solve(file)
