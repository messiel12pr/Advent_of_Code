import sys
data = sys.stdin.read().splitlines()

def evaluate(val, nums, curr):
    if not nums and curr == val:
        return True

    if not nums or curr > val:
        return False

    return evaluate(val, nums[1:], nums[0] * curr) or evaluate(val, nums[1:], nums[0] + curr)

def part_1():
    res = 0
    for line in data:
        val, nums = line.split(':')
        val = int(val)
        nums = list(map(int, nums.split()))
        
        if evaluate(val, nums, 0):
            res += val

    print(res)

part_1()