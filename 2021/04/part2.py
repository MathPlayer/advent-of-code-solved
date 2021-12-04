import sys
# filename = 'input-test.txt'
filename = 'input.txt'
data = [line.strip() for line in open(filename, 'r').readlines()]

# Parse
numbers = [int(x) for x in data[0].split(',')]
boards = []
board = []
for line in data[1:]:
    if not line:
        if board:
            boards.append(board)
        board = []
        continue
    board.append([int(x) for x in line.split()])

# Constants
w = len(boards[0][0])
h = len(boards[0])
count = len(boards)
MARKED = -1


def print_exit(board, mark):
    s = sum([x for line in board for x in line if x != MARKED])
    print(f"{s=},{mark=},{s*mark=}")
    sys.exit(0)


# Get all wins
won_boards = {}
last = None

for number in numbers:
    # Early exit
    if len(won_boards) == count:
        break

    # Mark the matches
    for index, board in enumerate(boards):
        # Skip won boards
        if index in won_boards:
            continue

        # Mark
        for i in range(h):
            for j in range(w):
                if board[i][j] == number:
                    boards[index][i][j] = MARKED

    # Check bingo
    for index, board in enumerate(boards):
        # Skip won boards
        if index in won_boards:
            continue
        # lines
        won = False
        for i, line in enumerate(board):
            if max(line) == MARKED:
                won_boards[index] = number
                last = index
                won = True
                break
        if won:
            continue
        # columns
        for j in range(h):
            if max([board[i][j] for i in range(w)]) == MARKED:
                won_boards[index] = number
                last = index
                break

print_exit(boards[last], won_boards[last])
