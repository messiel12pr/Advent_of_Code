import sys


def binary_search(num, ranges):
    res = 0
    l, r = 0, len(ranges) - 1
    while l <= r:
        m = (l + r) // 2
        lower, upper = ranges[m]
        if num in range(lower, upper + 1):
            return 1
        
        elif num > upper:
            l = m + 1

        else:
            r = m - 1

    return 0


def part_1():
    line = sys.stdin.readline().strip()
    ranges = []

    while line:
        lower, upper = map(int, line.split('-'))
        ranges.append((lower, upper))
        line = sys.stdin.readline().strip()
    
    ranges = sorted(ranges)
    merged_ranges = []

    last_lower, last_upper = ranges[0]
    i = 1
    while i < len(ranges):
        lower, upper = ranges[i]
        if lower <= last_upper:
            last_upper = max(last_upper, upper)

        else:
            merged_ranges.append((last_lower, last_upper))
            last_lower, last_upper = ranges[i]
        i += 1
    merged_ranges.append((last_lower, last_upper))

    line = sys.stdin.readline().strip()
    res = 0
    while line:
        id = int(line)
        res += binary_search(id, merged_ranges)
        line = sys.stdin.readline().strip()

    return res

#print(part_1())

def part_2():
    line = sys.stdin.readline().strip()
    ranges = []

    while line:
        lower, upper = map(int, line.split('-'))
        ranges.append((lower, upper))
        line = sys.stdin.readline().strip()
    
    ranges = sorted(ranges)
    merged_ranges = []

    last_lower, last_upper = ranges[0]
    i = 1
    while i < len(ranges):
        lower, upper = ranges[i]
        if lower <= last_upper:
            last_upper = max(last_upper, upper)

        else:
            merged_ranges.append((last_lower, last_upper))
            last_lower, last_upper = ranges[i]
        i += 1
    merged_ranges.append((last_lower, last_upper))

    res = 0

    for lower, upper in merged_ranges:
        res += (upper + 1) - lower

    return res

print(part_2())