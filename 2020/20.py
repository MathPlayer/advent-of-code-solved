#!/usr/bin/env python

import sys

from itertools import permutations, combinations
from math import sqrt, prod

def left(tile):
    ''' Returns first column of the tile. '''
    return tuple(x[0] for x in tile)


def right(tile):
    ''' Returns last column of the tile. '''
    return tuple(x[-1] for x in tile)


def top(tile):
    ''' Returns first row of the tile. '''
    return tuple(tile[0])


def bottom(tile):
    ''' Returns last row of the tile. '''
    return tuple(tile[-1])


def rotate(tile):
    ''' Rotates a tile 90 degrees. '''
    return tuple(tuple(tile[y][len(tile[0]) - x - 1] for y in range(len(tile))) for x in range(len(tile[0])))


def flip_h(tile):
    ''' Flips a tile horizontally. '''
    return tuple(tuple(tile[y][len(tile[0]) - x - 1] for x in range(len(tile[0]))) for y in range(len(tile)))


def flip_v(tile):
    ''' Flips a tile vertically. '''
    return tuple(tuple(tile[len(tile) - y - 1][x] for x in range(len(tile[0]))) for y in range(len(tile)))


def all_rotations(tile):
    ''' Combine flips and rotations in all possible ways. Some might be duplicates. '''
    return set([
        tile, rotate(tile), rotate(rotate(tile)), rotate(rotate(rotate((tile)))),
        flip_h(tile), rotate(flip_h(tile)), rotate(rotate(flip_h(tile))), rotate(rotate(rotate((flip_h(tile))))),
        flip_v(tile), rotate(flip_v(tile)), rotate(rotate(flip_v(tile))), rotate(rotate(rotate((flip_v(tile)))))
    ])


def match(hay, y, x, needle, mark):
    ''' Checks if the needle matches the hay at x, y coords. '''
    for j, line in enumerate(needle):
        for i, c in enumerate(line):
            if c == mark and hay[y + j][x + i] != mark:
                return False
    return True


def count(matrix, c):
    ''' Count occurences of character c in the matrix. '''
    return sum(c == '#' for line in matrix for c in line)

def read(in_file):
    ''' Reads data for day 20. '''
    data = {}
    with open(in_file) as f:
        for line in map(lambda x: x.strip(), f.readlines()):
            if not line:
                continue
            if "Tile" in line:
                index = int(line[4:-1])
                data[index] = []
            else:
                data[index].append(line)

    return {index: tuple(tuple(c for c in line) for line in value) for index, value in data.items()}


def solve(in_file):
    ''' Solves day 20. '''
    tiles = read(in_file)
    print(f"--- {in_file}")
    size = int(sqrt(len(tiles)))
    tile_height = len(list(tiles.values())[0])
    tile_width = len(list(tiles.values())[0][0])

    # Create a dictionary with key = border, value = set of tile indices having that margin.
    matches = {}
    for index, tile in tiles.items():
        margins = {func(tile) for func in (left, right, top, bottom)}
        for value in margins:
            if value not in matches:
                matches[value] = set()
            matches[value].add(index)
            rev = tuple(reversed(value))
            if rev not in matches:
                matches[rev] = set()
            matches[rev].add(index)

    # Create a dictionary with key = tile index, value = set of neighboring indices.
    neighbors = {}
    for index in tiles:
        tile_matches = set()
        for k in matches.values():
            if len(k) != 2:
                continue
            if index in k:
                tile_matches |= k
        neighbors[index] = tile_matches - {index}

    # Print part 1
    corners = {x for x, y in neighbors.items() if len(y) == 2}
    print(prod(corners))

    # Build the (rotated, flipped) matrix of image indices.
    indices = [[None for _ in range(size)] for _ in range(size)]
    picked = set()
    for y in range(size):
        for x in range(size):
            if x == 0 and y == 0:
                # Pick one corner at random to be top left.
                pick = corners.pop()
                picked.add(pick)
                indices[y][x] = pick
                continue

            # Compute the count of neighbors.
            if (x == size - 1 and y in [0, size - 1]) or (y == size - 1 and x in [0, size - 1]):
                neigh_count = 2
            elif x == 0 or y == 0 or x == size - 1 or y == size - 1:
                neigh_count = 3
            else:
                neigh_count = 4

            # Find what's filled towards top and left.
            filled = set()
            if y > 0 and indices[y - 1][x] != None:
                filled.add(indices[y - 1][x])
            if x > 0 and indices[y][x - 1] != None:
                filled.add((indices[y][x - 1]))
            # Find a tile index which is not picked and has as neighbors the filled set.
            for index, neigh in neighbors.items():
                if index not in picked and len(neigh) == neigh_count and not filled - neigh:  # All filled are in neigh
                    picked.add(index)
                    indices[y][x] = index
                    break
            if not indices[y][x]:
                raise NotImplementedError(f"This should never happen ({y} {x})")

    # Build the (rotated, flipped) matrix of tiles.
    image_tiles = [[None for _ in range(size)] for _ in range(size)]
    for y in range(size):
        for x in range(size):
            index = indices[y][x]
            tile_rotations = all_rotations(tiles[index])
            to_remove = set()
            # Check with left neigh.
            if x > 0:
                neigh_rotations = [image_tiles[y][x - 1]]
                if not neigh_rotations[0]:
                    neigh_rotations = all_rotations(tiles[indices[y][x - 1]])
                for i, rot in enumerate(tile_rotations):
                    if not any(left(rot) == right(neigh_rot) for neigh_rot in neigh_rotations):
                        to_remove.add(i)
            # Check with right neigh.
            if x < size - 1:
                neigh_rotations = [image_tiles[y][x + 1]]
                if not neigh_rotations[0]:
                    neigh_rotations = all_rotations(tiles[indices[y][x + 1]])
                for i, rot in enumerate(tile_rotations):
                    if not any(right(rot) == left(neigh_rot) for neigh_rot in neigh_rotations):
                        to_remove.add(i)
            # Check with top neigh.
            if y > 0:
                neigh_rotations = [image_tiles[y - 1][x]]
                if not neigh_rotations[0]:
                    neigh_rotations = all_rotations(tiles[indices[y - 1][x]])
                for i, rot in enumerate(tile_rotations):
                    if not any(top(rot) == bottom(neigh_rot) for neigh_rot in neigh_rotations):
                        to_remove.add(i)
            # Check with bottom neigh.
            if y < size - 1:
                neigh_rotations = [image_tiles[y + 1][x]]
                if not neigh_rotations[0]:
                    neigh_rotations = all_rotations(tiles[indices[y + 1][x]])
                for i, rot in enumerate(tile_rotations):
                    if not any(bottom(rot) == top(neigh_rot) for neigh_rot in neigh_rotations):
                        to_remove.add(i)

            for index, tile in enumerate(tile_rotations):
                if index not in to_remove:
                    image_tiles[y][x] = tile
                    break

            # print(y, x, len(tile_rotations), len(to_remove), to_remove)

    # Assemble the image.
    image = [['@' for _ in range(size * (tile_width - 2))] for _ in range(size * (tile_height - 2))]
    for y in range(size):
        for x in range(size):
            for j, line in enumerate(image_tiles[y][x]):
                if j in [0, tile_height - 1]:
                    continue
                for i, c in enumerate(line):
                    if i in [0, tile_width - 1]:
                        continue
                    image[y * (tile_height - 2) + j - 1][x * (tile_width - 2) + i - 1] = c
    image = tuple(tuple(c for c in line) for line in image)

    # Find the monsters.
    monster = tuple(tuple(c for c in line) for line in [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '])

    for img in all_rotations(image):
        monsters = 0
        for y in range(len(img) - len(monster)):
            for x in range(len(img[0]) - len(monster[0])):
                # Monsters can overlap? Assuming yes.
                if match(img, y, x, monster, '#'):
                    monsters += 1
        if monsters:
            # Asssume only one rotation of the image has monsters.
            print(count(img, '#') - monsters * count(monster, '#'))
            return


if __name__ == '__main__':
    solve('20test.in')
    solve('20.in')

    sys.exit(0)
