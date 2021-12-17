from math import inf

filename = 'input-test.txt'
filename = 'input.txt'
line = [line.strip() for line in open(filename, 'r').readlines()][0]

x, y = line.split(':')[1].lstrip().split(', ')
ax_min, ax_max = [int(v) for v in x.split('=')[1].split('..')][:2]
ay_min, ay_max = [int(v) for v in y.split('=')[1].split('..')][:2]

print(f"{ax_min=} {ax_max=} {ay_min=} {ay_max=}")

result = -inf

vx_range = max(abs(ax_min), abs(ax_max)) + 1
vy_range = max(abs(ay_min), abs(ay_max)) + 1
for vx_0 in range(-vx_range, vx_range):
    for vy_0 in range(-vy_range, vy_range):
        x, y = 0, 0
        max_y = 0
        vx, vy = vx_0, vy_0
        while y >= ay_min:
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            elif vx < 0:
                vx += 1
            vy -= 1
            max_y = max(max_y, y)
            if ax_min <= x <= ax_max and ay_min <= y <= ay_max:
                result = max(result, max_y)
                break

print(f"{result=}")
