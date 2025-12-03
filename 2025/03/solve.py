#!/usr/bin/env python

def read_input(file_path):
    with open(file_path, 'r') as file:
        raw = file.read()

    parsed = raw.splitlines()
    return parsed


def solve(file_path):
    print(f"Solving for {file_path}...")
    data = read_input(file_path)

    # Part 1
    max_values = []
    for i, line in enumerate(data):
        best_line_value = 0
        for a in range(len(line)):
            for b in range(a + 1, len(line)):
                candidate = int(line[a] + line[b])
                if candidate > best_line_value:
                    best_line_value = candidate
        max_values.append(best_line_value)

    print(f"{sum(max_values)}")

    # part 2
    max_values = []
    for i, line in enumerate(data):
        stack = []
        to_remove = len(line) - 12
        for d in line:
            while stack and to_remove > 0 and int(stack[-1]) < int(d):
                stack.pop()
                to_remove -= 1
            stack.append(d)
        max_values.append(int(''.join(stack[:12])))

    print(f"{sum(max_values)}")


if __name__ == "__main__":
    file = "test"
    solve(file)

    file = "input"
    solve(file)
