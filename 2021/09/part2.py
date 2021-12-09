from collections import deque

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

lows = {}
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
            lows[(i, j)] = crt

# Sort lows on height.
lows = {k: v for k, v in sorted(lows.items(), key=lambda item: item[1])}

visited = set()
basins = []
for (x, y), val in lows.items():
    if (x, y) in visited:
        # Low point in another basin
        continue

    # Do BFS.
    basin = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        top_x, top_y = queue.popleft()
        visited.add((top_x, top_y))
        for i, j in NEIGH:
            n_x, n_y = top_x + i, top_y + j
            if 0 <= n_x < rows and 0 <= n_y < cols:
                if (n_x, n_y) in visited:
                    continue
                if heightmap[n_x][n_y] == 9:
                    continue
                basin += 1
                queue.append((n_x, n_y))
                visited.add((n_x, n_y))
    basins.append(basin)

basins = sorted(basins)
print(f"{basins[-1] * basins[-2] * basins[-3]=}")
