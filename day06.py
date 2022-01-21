with open("day06_input.txt") as f:
    this_line: list = [line.strip() for line in f]

fish_array = [int(i) for i in this_line[0].split(",")]

for _ in range(80):
    for fish in range(len(fish_array)):
        if fish_array[fish] > 0:
            fish_array[fish] -= 1
        else:
            fish_array[fish] += 6
            fish_array.append(8)


print(len(fish_array))
