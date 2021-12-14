from collections import Counter, defaultdict
filename = 'input-test.txt'
filename = 'input.txt'
lines = [line.strip() for line in open(filename, 'r').readlines()]

rules = {}
for line in lines:
    if '->' in line:
        left, right = line.split(' -> ')
        rules[left] = right
    elif line:
        raw_polymer = line

polymer = Counter()
for i, c in enumerate(raw_polymer[:-1]):
    polymer[raw_polymer[i:i+2]] += 1

for step in range(40):
    new_polymer = polymer.copy()
    for pair, count in polymer.items():
        if pair in rules:
            new_polymer[pair] -= count
            new_polymer[pair[0] + rules[pair]] += count
            new_polymer[rules[pair] + pair[1]] += count
    polymer = new_polymer.copy()

count = defaultdict(int)
for pair, value in polymer.items():
    count[pair[0]] += value
    count[pair[1]] += value

# All pairs count twice the characters, except for the start/end of the polymer.
count = {k: v // 2 for k, v in count.items()}
count[raw_polymer[0]] += 1
count[raw_polymer[-1]] += 1

max_value = max(count.values())
min_value = min(count.values())
print(f"{max_value} - {min_value} = {max_value - min_value}")
