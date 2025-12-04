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

        if direction == 'L':
            dial -= distance

        else:
            dial += distance

        if dial in range(-99, 1, 1):
            res += 1

        else:
            res += abs(dial)//100

        dial = dial % 100
        line = sys.stdin.readline().strip()

    return res

#print(part_1())
print(part_2())

