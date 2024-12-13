#!/usr/bin/env python3


def read(filename):
    content = open(filename).read()
    lines = [x.strip() for x in content.split('\n')]

    data = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            data[(i, j)] = c

    return data


def get_region(data, coords):
    region = set()
    stack = [coords]
    while stack:
        x, y = stack.pop()
        if (x, y) in region:
            continue
        region.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in data and data[(new_x, new_y)] == data[coords]:
                stack.append((new_x, new_y))

    return region


def cost(region):
    area = len(region)
    perimeter = 0

    for x, y in region:
        neighbors = 0
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (x + dx, y + dy) in region:
                neighbors += 1
        perimeter += 4 - neighbors

    return area * perimeter


def merge_edges(edges):
    merged_edges = []
    for i in range(len(edges)):
        edge_i, relative_position_i = edges[i]
        for j in range(i + 1, len(edges)):
            edge_j, relative_position_j = edges[j]
            if relative_position_i == relative_position_j and edge_i & edge_j:
                edge_i |= edge_j
                edge_j.clear()
            if edge_i:
                merged_edges.append((edge_i, relative_position_i))

    return merged_edges


def cost_2(region):
    area = len(region)

    # tuple of (set of points, relative position (e.g. up, down, left, right) from the points).
    edges = []
    for x, y in region:
        # Cell neighbors (adding)
        neighbors = {'left': set(), 'right': set(), 'up': set(), 'down': set()}

        # Edges outside the region (removing)
        cell_external_edges = {'left', 'right', 'up', 'down'}

        # Neighbors that share the same type of edge with the cell (adding)
        neighbors_sharing_edge = {'left': set(), 'right': set(), 'up': set(), 'down': set()}
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor_cell = x + dx, y + dy
            if neighbor_cell in region:
                if dx == 0:
                    if dy == 1:
                        neighbors['right'].add(neighbor_cell)
                        cell_external_edges.remove('right')
                        neighbors_sharing_edge['up'].add(neighbor_cell)
                        neighbors_sharing_edge['down'].add(neighbor_cell)
                    else:
                        neighbors['left'].add(neighbor_cell)
                        cell_external_edges.remove('left')
                        neighbors_sharing_edge['up'].add(neighbor_cell)
                        neighbors_sharing_edge['down'].add(neighbor_cell)
                else:
                    if dx == 1:
                        neighbors['down'].add(neighbor_cell)
                        cell_external_edges.remove('down')
                        neighbors_sharing_edge['left'].add(neighbor_cell)
                        neighbors_sharing_edge['right'].add(neighbor_cell)
                    else:
                        neighbors['up'].add(neighbor_cell)
                        cell_external_edges.remove('up')
                        neighbors_sharing_edge['left'].add(neighbor_cell)
                        neighbors_sharing_edge['right'].add(neighbor_cell)

        if not cell_external_edges:
            continue

        # For each edge orientation, check if there's another edge that should contain this neighbor.
        for cell_external_edge in cell_external_edges:
            found = False
            for edge, relative_position in edges:
                if relative_position != cell_external_edge:
                    continue

                for neighbor in neighbors_sharing_edge[cell_external_edge]:
                    if neighbor in edge:
                        found = True
                        edge.add((x, y))
                        break
            if not found:
                edges.append((set([(x, y)]), cell_external_edge))

        # Some edges might be the same, merge.
        edges = merge_edges(edges)

    return area * len(edges)


def part_1(data):
    result = 0

    visited = set()
    for coords in data:
        if coords in visited:
            continue
        region = get_region(data, coords)
        visited |= region
        result += cost(region)

    return result


def part_2(data):
    result = 0

    visited = set()
    for coords in data:
        if coords in visited:
            continue
        region = get_region(data, coords)
        visited |= region
        result += cost_2(region)

    return result


def solve(filename):
    data = read(filename)

    print("part 1:")
    result = part_1(data)
    print(result)

    print("part 2:")
    result = part_2(data)
    print(result)


if __name__ == '__main__':
    # solve('test')
    # solve('test2')
    # solve('test3')
    solve('input')
