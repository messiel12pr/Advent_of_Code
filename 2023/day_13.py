
def start_horizontal(grid):
    for row in range(0, len(grid) - 1, 1):
        if grid[row] == grid[row + 1]:
            if is_valid_mirror_horizontal(grid, row, row + 1):
                return (row, row + 1)
    return (0, 0)

def is_valid_mirror_horizontal(grid, r1, r2):
    if r1 < 0 or r2 > len(grid) - 1:
        return True
    
    if grid[r1] == grid[r2]:
        return is_valid_mirror_horizontal(grid, r1 - 1, r2 + 1)

    return False

def start_vertical(grid):
    for column in range(0, len(grid[0]) - 1, 1):
        if [grid[i][column] for i in range(len(grid))] == [grid[i][column + 1] for i in range(len(grid))]:
            if is_valid_mirror_vertical(grid, column, column + 1):
                return (column, column + 1)

    return (0, 0)

def is_valid_mirror_vertical(grid, c1, c2):
    if c1 < 0 or c2 > len(grid[0]) - 1:
        return True
    
    if [grid[i][c1] for i in range(len(grid))] == [grid[i][c2] for i in range(len(grid))]:
        return is_valid_mirror_vertical(grid, c1 - 1, c2 + 1)
    
    return False

def part_a():
    with open('input.txt', 'r') as file:
        result_rows = 0
        result_cols = 0
        
        for pattern in file.read().split('\n\n'):
            grid = pattern.splitlines()
            start_h = start_horizontal(grid)
            start_v = start_vertical(grid)

            if start_h != (0, 0):
                result_rows += start_h[1]

            if start_v != (0, 0):
                result_cols += start_v[1]

        print(result_cols + 100 * result_rows)

part_a()