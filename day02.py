lines = []

with open('day02_input.txt') as f:
    lines = f.readlines()

x_pos = 0;
y_pos = 0;
aim = 0;

for line in lines:
    dir = str(line[0])
    dir_chunks = line.split(' ')
    amount = int(dir_chunks[1])

    if(dir == "f"):
        x_pos = x_pos + amount
        y_pos = y_pos + (aim * amount)
    elif(dir == "u"):
        #Part 1 calculation
        #y_pos = y_pos - amount
        aim = aim - amount;
    elif(dir == "d"):
        #Part 1 calculation
        #y_pos = y_pos + amount
        aim = aim + amount;

my_position = x_pos * y_pos
print(my_position)
