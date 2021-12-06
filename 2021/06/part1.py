filename = 'input-test.txt'
filename = 'input.txt'
fish = [int(x) for x in open(filename, 'r').read().strip().split(',')]

days = 18
days = 80

for day in range(days):
    update_fish = []
    new_fish = []
    for f in fish:
        if f == 0:
            update_fish.append(6)
            new_fish.append(8)
        else:
            update_fish.append(f - 1)
    fish = update_fish + new_fish
    print(f"After {day+1:02d} days: {len(fish)}")
