import statistics

with open("day07_input.txt") as f:
    this_line: list = [line.strip() for line in f]

crab_locations = [int(i) for i in this_line[0].split(",")]
spent_fuel = 0


def calc_average(lst):
    return statistics.median(crab_locations)


desired_location = calc_average(crab_locations)


for crab in range(len(crab_locations)):
    spent_fuel += abs(crab_locations[crab] - desired_location)


print(spent_fuel)
