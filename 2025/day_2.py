import sys

def part_1():
    test_cases = sys.stdin.readline().strip().split(',')

    # incomplete
    for case in test_cases:
        lower, upper = map(int, case.split('-'))
