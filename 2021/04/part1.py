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


for number in numbers:
    # Mark the matches
    for index, board in enumerate(boards):
        for i in range(h):
            for j in range(w):
                if board[i][j] == number:
                    boards[index][i][j] = MARKED
    # Check bingo
    for index, board in enumerate(boards):
        # Lines
        for i, line in enumerate(board):
            if max(line) == MARKED:
                print_exit(board, number)
        # Columns
        for j in range(h):
            if max([board[i][j] for i in range(w)]) == MARKED:
                print_exit(board, number)
