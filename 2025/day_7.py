import sys

def part_1():
    grid = [line.strip() for line in sys.stdin.readlines()]
    splits = [False for _ in range(len(grid[0]))]
    splits[grid[0].index('S')] = True
    res = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '^' and splits[col]:
                splits[col] = False
                if col - 1 in range(len(splits)):
                    splits[col - 1] = True

                if col + 1 in range(len(splits)):
                    splits[col + 1] = True
                res += 1
    return res

#print(part_1())


def part_2():
    grid = [line.strip() for line in sys.stdin.readlines()]
    hm = {}

    def rec(beam, row):
        if row >= len(grid) or beam not in range(len(grid[0])):
            return 0
        
        if (row, beam) in hm:
            return hm[(row, beam)]
        
        if grid[row][beam] == '^':
            curr = rec(beam - 1, row + 1) + rec(beam + 1, row + 1) + 1
            hm[(row, beam)] = curr
            return curr

        return rec(beam, row + 1)

    beam = grid[0].index('S')
    return rec(beam, 1) + 1

print(part_2())
