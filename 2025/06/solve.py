#!/usr/bin/env python

from math import prod


def read_input(file_path):
    with open(file_path, 'r') as file:
        raw = file.read()

    numbers = []
    ops = []
    for line in raw.splitlines():
        if any(c.isdigit() for c in line):
            numbers.append(line.strip().split())
        else:
            ops = line.strip().split()
    return numbers, ops


def solve_1(numbers, ops):
    numbers = [[int(x) for x in line] for line in numbers]
    results = {i: None for i in range(len(ops))}
    for i in range(len(ops)):
        for j, number_line in enumerate(numbers):
            crt = results[i]
            if not crt:
                crt = number_line[i]
            else:
                if ops[i] == '+':
                    crt += number_line[i]
                elif ops[i] == '*':
                    crt *= number_line[i]
            results[i] = crt
    return sum(results.values())


def read_input_2(file_path):
    with open(file_path, 'r') as file:
        raw = file.read()

    numbers_raw = []
    ops = []
    for line in raw.splitlines():
        if any(c.isdigit() for c in line):
            numbers_raw.append(line.rstrip('\n'))
        else:
            ops = line.strip().split()

    return numbers_raw, ops


def solve_2(numbers_raw, ops):
    col_indices = []
    for col in range(len(numbers_raw[0])):
        if all(line[col] == ' ' for line in numbers_raw):
            col_indices.append(col)

    col_indices.append(len(numbers_raw[0]))

    numbers = []
    for i in range(len(col_indices)):
        if i == 0:
            start = 0
            end = col_indices[i]
        else:
            start = col_indices[i-1] + 1
            end = col_indices[i]

        op_numbers = []
        for col in range(start, end):
            number = int(''.join((line[col] for line in numbers_raw)))
            op_numbers.append(number)
        numbers.append(op_numbers)

    results = []
    for i in range(len(ops)):
        if ops[i] == '+':
            results.append(sum(numbers[i]))
        elif ops[i] == '*':
            results.append(prod(numbers[i]))
    return sum(results)


def solve(file_path):
    print(f">>>> {file_path}")
    print("part 1")
    numbers, ops = read_input(file_path)
    print(solve_1(numbers, ops))

    print("part 2")
    numbers_raw, ops = read_input_2(file_path)
    print(solve_2(numbers_raw, ops))


if __name__ == "__main__":
    file = "test"
    solve(file)

    file = "input"
    solve(file)
