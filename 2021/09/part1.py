filename = 'input-test.txt'
filename = 'input.txt'
lines = [line.strip() for line in open(filename, 'r').readlines()]

heightmap = [[int(x) for x in line] for line in lines]
cols = len(heightmap[0])
rows = len(heightmap)

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, 1)
DOWN = (0, -1)
NEIGH = [LEFT, RIGHT, UP, DOWN]

result = 0
for i in range(rows):
    for j in range(cols):
        crt = heightmap[i][j]
        low = True
        for x, y in NEIGH:
            n_i, n_j = i + x, j + y
            if 0 <= n_i < rows and 0 <= n_j < cols and heightmap[n_i][n_j] <= crt:
                low = False
                break
        if low:
            result += crt + 1

print(f"{result=}")
