import sys
data = sys.stdin.read().splitlines()

def search(row, col):
    ctr = 0

    normal = [(0, 1), (0, 2), (0, 3)]
    backwards = [(0, -1), (0, -2), (0, -3)]

    upwards = [(-1, 0), (-2, 0), (-3, 0)]
    diagonal_up_right = [(-1, 1), (-2, 2), (-3, 3)]
    diagonal_up_left = [(-1, -1), (-2, -2), (-3, -3)]

    downwards = [(1, 0), (2, 0), (3, 0)]
    diagonal_down_right = [(1, 1), (2, 2), (3, 3)]
    diagonal_down_left = [(1, -1), (2, -2), (3, -3)]

    coords = [normal, backwards, upwards, diagonal_up_right, diagonal_up_left, 
              downwards,diagonal_down_right, diagonal_down_left]

    for coord in coords:
        i = 1
        XMAS = 'XMAS'

        for r, c in coord:
            row2, col2 = row + r, col + c
            if row2 in range(len(data)) and col2 in range(len(data[0])) and data[row2][col2] == XMAS[i]:
                i += 1

        if i == 4:
            ctr += 1

    return ctr


def search2(row, col):
    pass


def part_1():
    res = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == 'X':
                res += search(row, col)

    print(res)


def part_2():
    res = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == 'X':
                res += search2(row, col)

    print(res)

part_1()
part_2()