import sys


def part_1():
    res = 0
    dial = 50
    line = sys.stdin.readline().strip()
    while line:
        direction, distance = line[0], int(line[1:])

        if direction == 'L':
            dial -= distance

        else:
            dial += distance

        dial = dial % 100
        if dial == 0:
            res += 1


        line = sys.stdin.readline().strip()

    return res


def part_2():
    # res: 6027
    res = 0
    dial = 50
    line = sys.stdin.readline().strip()
    while line:
        direction, distance = line[0], int(line[1:])
        prev_dial = dial

        if direction == 'L':
            dial -= distance

        else:
            dial += distance

        
        if distance > 100:
            if dial < 0:
                res += (distance + prev_dial) // 100

            else:
                res += dial // 100

        else:
            if dial == 0 or (prev_dial > 0 and dial < 0) or dial >= 100:
                res += 1
        
        #print(prev_dial, dial, distance, res)

        dial = dial % 100
        line = sys.stdin.readline().strip()

    return res

#print(part_1())
print(part_2())

