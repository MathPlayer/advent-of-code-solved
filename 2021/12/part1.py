from collections import defaultdict, deque

filename = 'input-test.txt'
filename = 'input.txt'
lines = [line.strip().split('-') for line in open(filename, 'r').readlines()]

graph = defaultdict(set)
for start, end in lines:
    graph[start].add(end)
    graph[end].add(start)


stack = deque()
stack.append(['start'])
result = 0
while stack:
    path = stack.popleft()
    for neigh in graph[path[-1]]:
        if neigh == 'end':
            result += 1
            # print(f"found way #{result}: {path + ['end']}")
            continue
        if neigh in path and neigh.upper() != neigh:
            continue
        stack.append(path + [neigh])

print(f"{result=}")
