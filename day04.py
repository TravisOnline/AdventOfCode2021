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
        for i in row:
            if i[0] == number:
                i[1] = True
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
    score = 0
    for row in board:
        for i in row:
            if not i[1]:
                score += i[0]
    return score * number


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
