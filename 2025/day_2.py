import sys

def part_1():
    test_cases = sys.stdin.readline().strip().split(',')
    res = 0

    for case in test_cases:
        lower, upper = map(int, case.split('-'))
        for num in range(lower, upper + 1):
            str_num = str(num)
            if str_num[:(len(str_num)//2)] * 2 == str_num:
                res += num

    return res


def part_2():
    test_cases = sys.stdin.readline().strip().split(',')
    res = 0

    for case in test_cases:
        lower, upper = map(int, case.split('-'))
        for num in range(lower, upper + 1):
            str_num = str(num)

            for i in range(1, (len(str_num)//2) + 1):
                if str_num[:i] * (len(str_num)//i) == str_num:
                    res += num
                    break
    return res

#print(part_1())
print(part_2())