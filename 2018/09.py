#!/usr/bin/env python3

def solve(players, last_marble):
    print("Solving for {} players and {} last marble".format(players, last_marble))
    game = [0, 1]
    index = 1
    player = 0
    scores = [0] * players

    for x in range(2, last_marble + 1):
        player = (player + 1) % players
        # print("[{}] {}".format(player + 1, game))
        if 0 == x % 23 and x:
            inc = x
            remove_index = (x + index - 7) % len(game)
            inc += game[remove_index]
            print("removing {}".format(game[remove_index]))
            del game[remove_index]
            index = remove_index
            scores[player] += inc
            print("scores after update{}".format(scores))
        else:
            index = (index + 2) % len(game)
            if index == 0:
                index = len(game)
            game.insert(index, x)


solve(9, 32)
solve(10, 1618)
# solve(13, 7999)


from collections import deque, defaultdict

def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])
    player = 0

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

        player = (player + 1) % max_players

    return max(scores.values()) if scores else 0


print(play_game(9, 32))
print(play_game(10, 1618))
print(play_game(424, 71144))
print(play_game(424, 7114400))
