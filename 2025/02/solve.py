#!/usr/bin/env python

def read_input(file_path):
    with open(file_path, 'r') as file:
        raw = file.read()

    result = []
    for id_range in raw.split(','):
        id_range_list = id_range.split('-')
        a = int(id_range_list[0])
        b = int(id_range_list[1])
        result.append((a, b))
    return result


def is_invalid_id(n):
    string = str(n)
    length = len(string)

    if length % 2 != 0:
        return False
    if string[:length // 2] != string[length // 2:]:
        return False

    return True


def count_invalid_ranges(data, is_invalid_func):
    result = 0
    for (a, b) in data:
        # count = 0
        for i in range(a, b + 1):
            if is_invalid_func(i):
                # count += 1
                result += i
        # print(f"Range {a}-{b}: {count}")
    print(result)


def is_invalid_id_2(n):
    string = str(n)

    for size in range(1, len(string) // 2 + 1):
        for start in range(len(string) - 2 * size + 1):
            substring = string[start:start + size]
            repeated = substring * (len(string) // size)
            if repeated == string:
                return True

    return False


def solve(file_path):
    print(f"Solving for file {file_path}")
    data = read_input(file_path)

    count_invalid_ranges(data, is_invalid_id)
    count_invalid_ranges(data, is_invalid_id_2)


if __name__ == "__main__":
    file = "test"
    solve(file)

    file = "input"
    solve(file)
