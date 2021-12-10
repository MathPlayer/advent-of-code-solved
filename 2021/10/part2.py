filename = 'input.txt'
# filename = 'input-test.txt'
lines = [line.strip() for line in open(filename, 'r').readlines()]

POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
OPEN = '([{<'
CLOSE = ')]}>'

result = []
for line in lines:
    stack = [line[0]]
    valid = True
    for c in line[1:]:
        if c in OPEN:
            stack.append(c)
            continue
        if not stack:
            raise Exception(f"Extraneous {c} in {line}")
        last = stack.pop()
        if OPEN.index(last) != CLOSE.index(c):
            valid = False
            break
    if not valid:
        continue
    score = 0
    while stack:
        last = stack.pop()
        score *= 5
        score += OPEN.index(last) + 1
    result.append(score)

result.sort()
print(f"{result[len(result) // 2]}")
