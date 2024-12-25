import sys
from collections import Counter

data = sys.stdin.read().splitlines()

def part_1():
    invalid = 0
    for line in data:
        ls = list(map(int, line.split()))
        increasing = False
        if ls[0] - ls[1] < 0:
            increasing = True

        for i in range(len(ls) - 1):
            if increasing and ls[i] - ls[i+1] not in range(-1, -4, -1) or not increasing and ls[i] - ls[i+1] not in range(1, 4, 1):
                invalid += 1
                break

    print(len(data) - invalid)


def part_2():
    
    res = 0
    for line in data:
        ls = list(map(int, line.split()))
        increasing = False
        if ls[0] - ls[1] < 0:
            increasing = True

        ls.insert(0, 0)
        for i in range(len(ls) - 1):
            invalid = False
            copy_ls = ls.copy()
            if i > 0:
                copy_ls.pop(0)
            copy_ls.pop(i)

            for j in range(len(copy_ls) - 1):
                if increasing and copy_ls[j] - copy_ls[j+1] not in range(-1, -4, -1) or not increasing and copy_ls[j] - copy_ls[j+1] not in range(1, 4, 1):
                    invalid = True
                    break

            if not invalid:
                res += 1
                break

    print(res)

part_1()
part_2()