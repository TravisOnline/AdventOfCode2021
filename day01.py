#Create an array of strings from the input txt document
lines = []

with open('input_01') as f:
    lines = f.readlines()

f.close()

#Convert the array of strings to an array of ints
lines_int = [int(this_string) for this_string in lines]

#declare a variable to store how many times the list increments
increments = 0

#iterate through our array of ints, keep a hold of index
for index, line in enumerate(lines_int):
    #check index bounds
    if(index+1 < len(lines_int) and index - 1 >= 0):
        previous_line = str(lines_int[index-1])
        current_line = str(line)
        next_line = str(lines_int[index+1])

        if(index != 0 and current_line > previous_line):
            increments = increments + 1
            print(current_line + " increased")
        else:
            print(current_line)
    #if at the start of the index, look ahead
    elif(index - 1 < 0):
        current_line = str(line)
        next_line = str(lines_int[index + 1])
        if(current_line < next_line):
            increments = increments + 1
    #if at the end of the index
    elif(index+1 == len(lines_int) and current_line > previous_line):
        previous_line = str(lines_int[index - 1])
        current_line = str(line)
        increments = increments + 1
        print(current_line + " increased")

print((increments))

#reset our counter
increments = 0
#declare variable to store our totals in
this_total = int(0)
prev_total = int(0)

for index, line in enumerate(lines_int):
    if(index+2 < len(lines_int)):
        this_line = int(line)
        next_line = int(lines_int[index+1])
        next_next_line = int(lines_int[index+2])
        this_total = this_line + next_line + next_next_line
        #if this is the first entry in the index, move to next index without comparing totals
        if(prev_total == 0):
            prev_total = this_total
        else:
            if(this_total > prev_total):
                increments = increments + 1

        prev_total = this_total

print((increments))