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

result = {k: 0 for k in POINTS}
for line in lines:
    stack = [line[0]]
    for c in line[1:]:
        if c in OPEN:
            stack.append(c)
            continue
        if not stack:
            raise Exception(f"Extraneous {c} in {line}")
        last = stack.pop()
        if OPEN.index(last) != CLOSE.index(c):
            result[c] += POINTS[c]
            break

# print(f"{result=}")
print(f"{sum(result.values())}")
