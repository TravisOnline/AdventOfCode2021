with open('day03_input.txt') as f:
    input = [i for i in f.read().strip().split('\n')]

def PowerCalculate():
    gamma = []
    epsilon = []

    for column in range(0, len(input[0])):
        zero = 0
        one = 0

        for substring in input:
            if substring[column] == '0':
                zero += 1
            else:
                one += 1

        if zero > one:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')

    gamma = ''.join(gamma)
    epsilon = ''.join(epsilon)

    powerUse = int(gamma, 2) * int(epsilon,2)
    return powerUse

print(PowerCalculate())