from collections import Counter
filename = 'input-test.txt'
filename = 'input.txt'
lines = [line.strip() for line in open(filename, 'r').readlines()]

rules = {}
for line in lines:
    if '->' in line:
        left, right = line.split(' -> ')
        rules[left] = right
    elif line:
        polymer = line

for step in range(10):
    new_polymer = polymer
    extra = 0
    for i, _ in enumerate(polymer):
        pair = polymer[i:i+2]
        if pair in rules:
            new_polymer = new_polymer[:extra + i] + pair[0] + rules[pair] + new_polymer[extra + i + 1:]
            extra += 1
    polymer = new_polymer

count = Counter(polymer)
max_value = max(count.values())
min_value = min(count.values())
print(f"{max_value} - {min_value} = {max_value - min_value}")
