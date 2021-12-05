from collections import defaultdict

filename = 'input-test.txt'
filename = 'input.txt'
data = []
draw_min_x = 99999
draw_max_x = 0
draw_min_y = 99999
draw_max_y = 0
for line in open(filename, 'r').readlines():
    c1, c2 = line.split(' -> ')
    x1, y1 = [int(x) for x in c1.split(',')]
    x2, y2 = [int(x) for x in c2.split(',')]
    draw_min_x = min(draw_min_x, x1, x2)
    draw_max_x = max(draw_max_x, x1, x2)
    draw_min_y = min(draw_min_y, y1, y2)
    draw_max_y = max(draw_max_y, y1, y2)
    data.append((x1, y1, x2, y2))

plane = defaultdict(int)


def draw_plane():
    for y in range(draw_min_y, draw_max_y + 1):
        line = ''
        for x in range(draw_min_x, draw_max_x + 1):
            if plane[(x, y)] == 0:
                line += '.'
            else:
                line += str(plane[(x, y)])
        print(line)


for (x1, y1, x2, y2) in data:
    if y1 == y2:
        # horizontal
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        for x in range(min_x, max_x + 1):
            plane[(x, y1)] += 1
    elif x1 == x2:
        # vertical
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        for y in range(min_y, max_y + 1):
            plane[(x1, y)] += 1

# draw_plane()

# Count points on plane with value >= 2
count = len([v for v in plane.values() if v >= 2])
print(f"{count=}")
