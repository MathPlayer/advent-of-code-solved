def draw(dots_set):
    max_x = max(x for x, _ in dots) + 1
    max_y = max(y for _, y in dots) + 1

    for j in range(max_y):
        for i in range(max_x):
            if (i, j) in dots:
                print("#", sep='', end='')
            else:
                print('.', sep='', end='')
        print()
    print(len(dots_set))


filename = 'input-test.txt'
filename = 'input.txt'
lines = [line.strip() for line in open(filename, 'r').readlines()]

dots = set()
folds = []
for line in lines:
    if ',' in line:
        x, y = line.split(',')
        dots.add((int(x), int(y)))
    elif '=' in line:
        sp = line.split('=')
        folds.append((sp[0][-1], int(sp[1])))

for axis, value in folds:
    if axis == 'x':
        index = 0
    else:
        index = 1

    new_dots = set()
    for pair in sorted(dots):
        new_pair = list(pair)
        if value < pair[index]:
            new_pair[index] = value - (pair[index] - value)
        new_dots.add(tuple(new_pair))
    dots = new_dots
    break

print(len(dots))
