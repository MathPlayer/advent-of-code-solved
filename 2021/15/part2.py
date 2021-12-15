DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1)
]

filename = 'input-test.txt'
filename = 'input.txt'
lines = [line.strip() for line in open(filename, 'r').readlines()]

values = {}
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        values[(row, col)] = int(c)
rows = len(lines)
cols = len(lines[0])

cave = {}
for node, value in values.items():
    for x in range(0, 5):
        for y in range(0, 5):
            new_node = node[0] + x * cols, node[1] + y * rows
            new_value = value
            for _ in range(x + y):
                new_value += 1
                if new_value > 9:
                    new_value = 1
            cave[new_node] = new_value
rows *= 5
cols *= 5
values = cave

visited = set()
to_visit = set()
node = (0, 0)
mins = {(0, 0): 0}
while len(mins) < rows * cols:
    # if not len(mins) % 1000:
    #     print(f"{len(mins)}")
    visited.add(node)
    to_visit.discard(node)
    for x, y in DIRECTIONS:
        new_node = node[0] + x, node[1] + y
        n_x, n_y = new_node
        if n_x < 0 or n_x >= cols or n_y < 0 or n_y >= rows or new_node in visited:
            continue
        dist = mins[node] + values[new_node]
        if new_node not in mins or mins[new_node] > dist:
            mins[new_node] = dist
            to_visit.add(new_node)
    node = min(to_visit, key=lambda x: mins[x])

print(mins[(rows - 1, cols - 1)])
