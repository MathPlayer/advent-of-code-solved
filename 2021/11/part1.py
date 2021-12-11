from collections import deque
from copy import deepcopy
filename = 'input.txt'
# filename = 'input-test.txt'
lines = [line.strip() for line in open(filename, 'r').readlines()]

energies = [[int(x) for x in line] for line in lines]
cols = len(energies[0])
rows = len(energies)


def print_mat(mat, size_rows, size_cols, spaced=False):
    print(">>>")
    for x in range(size_rows):
        for y in range(size_cols):
            if spaced:
                print(f"{mat[x][y]:3d}", end='')
            else:
                print(f"{mat[x][y]}", end='')
        print()


result = 0
for step in range(100):
    # Increase all by 1
    energies = deepcopy(energies)
    to_flash = deque()
    for y in range(rows):
        for x in range(cols):
            energies[x][y] += 1
            if energies[x][y] > 9:
                to_flash.append((x, y))

    # Do flashes
    flashed = set()
    while to_flash:
        flash_x, flash_y = to_flash.popleft()
        result += 1
        energies[flash_x][flash_y] = 0
        for delta_x in [-1, 0, 1]:
            for delta_y in [-1, 0, 1]:
                if not delta_x and not delta_y:
                    continue
                n_x = flash_x + delta_x
                n_y = flash_y + delta_y
                if n_x < 0 or n_x >= cols or n_y < 0 or n_y >= rows:
                    continue
                if (n_x, n_y) in flashed or (n_x, n_y) in to_flash:
                    continue
                energies[n_x][n_y] += 1
                if energies[n_x][n_y] > 9:
                    to_flash.append((n_x, n_y))
        flashed.add((flash_x, flash_y))

print(result)
