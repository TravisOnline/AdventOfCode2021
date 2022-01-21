answer = 0

with open("day04_input.txt") as f:
    this_line: list = [line.strip() for line in f]

bingo_numbers = [int(i) for i in this_line[0].split(",")]

f.close()


def create_boards() -> list:
    boards = []
    for i in this_line[1:]:
        if i:
            boards[-1].append([[int(j.strip()), False] for j in i.split()])
        else:
            boards.append([])

    return boards


def mark_numbers(board: list, number: int) -> list:
    for row in board:
        for v in row:
            if v[0] == number:
                v[1] = True
    return board


def check_winner(board: list) -> bool:
    for row in board:
        if all([j[1] for j in row]):
            return True

    for c in range(len(board[0])):
        if all([j[1] for j in [r[c] for r in board]]):
            return True

    return False


def calc_score(board: list, number: int) -> int:
    s = 0
    for row in board:
        for v in row:
            if not v[1]:
                s += v[0]
    return s * num


board_array = create_boards()


for num in bingo_numbers:
    for b in range(len(board_array)):
        board_array[b] = mark_numbers(board_array[b], num)
        if check_winner(board_array[b]):
            answer = calc_score(board_array[b], num)
            break
    else:
        continue
    break


print(answer)