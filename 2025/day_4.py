import sys

def part_1():
    grid = [line.strip() for line in sys.stdin.readlines()]
    res = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            ctr = 0
            if grid[row][col] == '@': 
                adjacent = [(row - 1, col), (row - 1, col + 1), (row, col + 1), (row + 1, col + 1), (row + 1, col), (row + 1, col - 1), (row, col - 1), (row - 1, col - 1)]
                for row_adj, col_adj in adjacent:
                    if row_adj in range(len(grid)) and col_adj in range(len(grid[0])) and grid[row_adj][col_adj] == '@':
                        ctr += 1

                if ctr < 4:
                    res += 1
    return res

#print(part_1())

def part_2():
    grid = [line.strip() for line in sys.stdin.readlines()]
    res = 0
    rolls = []
    for row in range(len(grid)):
        temp_row = []
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                temp_row.append(True)
            else:
                temp_row.append(False)
        rolls.append(temp_row)

    prev_res = -1
    while res != prev_res:
        prev_res = res

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                ctr = 0
                if rolls[row][col]: 
                    adjacent = [(row - 1, col), (row - 1, col + 1), (row, col + 1), (row + 1, col + 1), (row + 1, col), (row + 1, col - 1), (row, col - 1), (row - 1, col - 1)]
                    for row_adj, col_adj in adjacent:
                        if row_adj in range(len(grid)) and col_adj in range(len(grid[0])) and rolls[row_adj][col_adj]:
                            ctr += 1

                    if ctr < 4:
                        res += 1
                        rolls[row][col] = False
        
    return res

print(part_2())