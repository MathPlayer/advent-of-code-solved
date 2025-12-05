#!/usr/bin/env python

def read_input(file_path):
    with open(file_path, 'r') as file:
        raw = file.readlines()

    ranges = []
    ingredients = []

    for line in raw:
        line = line.strip()
        if not line:
            continue
        if '-' in line:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
        else:
            ingredients.append(int(line))

    return ranges, ingredients


def solve(file_path):
    print(f">>> {file_path} <<<")
    ranges, ingredients = read_input(file_path)

    print("part 1")
    count = 0
    for ingredient in ingredients:
        if any(start <= ingredient <= end for start, end in ranges):
            count += 1
    print(count)

    print("part 2")
    ranges.sort()
    merged_ranges = [list(ranges[0])]
    for start, end in ranges[1:]:
        prev_start, prev_end = merged_ranges[-1]
        if start <= prev_end + 1:
            merged_ranges[-1][1] = max(prev_end, end)
        else:
            merged_ranges.append([start, end])
    result = sum(end - start + 1 for start, end in merged_ranges)
    print(result)


if __name__ == "__main__":
    file = "test"
    solve(file)

    file = "input"
    solve(file)
