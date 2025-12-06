import math
import sys

def part_1():
    nums = []
    line = sys.stdin.readline().strip().split()
    while line[0] not in ('*', '+'):
        nums.append(list(map(int, line)))
        line = sys.stdin.readline().strip().split()

    operations = line
    res = 0
    for i in range(len(nums[0])):
        curr = 1 if operations[i] == '*' else 0

        for j in range(len(nums)):
            if operations[i] == '*':
                curr *= nums[j][i]

            else:
                curr += nums[j][i]
        
        res += curr
    return res

#print(part_1())


def part_2():
    nums = []
    line = sys.stdin.readline()
    while line[0] not in ('*', '+'):
        nums.append(line[:-1])
        line = sys.stdin.readline()

    op = line
    res = 0
    i = 0
    while i < len(op):
        if op[i] in ('*', '+'):
            operator = op[i]
            problem = []
            while i < len(op):
                num = []
                for row in range(len(nums)):
                    if nums[row][i] in ('123456789'):
                        num.append(nums[row][i])

                if num:
                    problem.append(num)

                if i + 1 >= len(op) or op[i + 1] in ('*', '+'):
                    break
                i += 1

            if operator == '+':
                res += sum([int(''.join(x)) for x in problem])

            else:
                res += math.prod([int(''.join(x)) for x in problem])

        else:
            i += 1

    return res

print(part_2())