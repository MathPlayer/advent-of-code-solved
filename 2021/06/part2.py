from collections import Counter

filename = 'input-test.txt'
filename = 'input.txt'
fishes = Counter([int(x) for x in open(filename, 'r').read().strip().split(',')])

days = 18
days = 80
days = 256

for day in range(days):
    update_fishes = Counter()
    new_fishes = 0
    for fish, count in fishes.items():
        if fish == 0:
            update_fishes[6] += count
            new_fishes += count
        else:
            update_fishes[fish - 1] += count
    update_fishes[8] += new_fishes
    fishes = update_fishes
    print(f"After {day+1:02d} days: {sum(fishes.values())}")
