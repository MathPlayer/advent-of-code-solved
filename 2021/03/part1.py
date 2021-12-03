# filename = 'input-test.txt'
filename = 'input.txt'
data = [x.strip() for x in open(filename, 'r').readlines()]
size = len(data[0])

counts = {i: [0, 0] for i in range(size)}
for s in data:
    for i, c in enumerate(s):
        counts[i][int(c)] += 1

gamma = ''
epsilon = ''
for k in range(size):
    if counts[k][0] > counts[k][1]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))
