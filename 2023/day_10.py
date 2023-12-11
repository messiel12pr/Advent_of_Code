def display_grid(grid, visited):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) in visited:
                print('0', end=' ')
            else:
                print(grid[r][c], end=' ')
        print()

def find_coord_S(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                return (r, c)
            
def part_a():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        
        directions = {'|':  [(1, 0), (-1, 0)],
                      '-':  [(0, -1), (0, 1)],
                      'L':  [(-1, 0), (0, 1)],
                      'J':  [(-1, 0), (0, -1)],
                      '7':  [(1, 0), (0, -1)],
                      'F':  [(1, 0), (0, 1)],
                      'S':  [(0, -1), (-1, 0), (0, 1), (1, 0)],
                      '.': []}

        connecting = {(0, -1): ['-', 'L', 'F'],
                      (-1, 0): ['|', '7', 'F'],
                      (0, 1):  ['-', 'J', '7'],
                      (1, 0):  ['|', 'L', 'J']}
        
        grid = [list(line) for line in input]
        start = find_coord_S(grid)
        visited = set(start)
        next_pipe = start
        steps = 0

        while next_pipe != None:
            curr_pipe = next_pipe
            
            for dir in directions[grid[curr_pipe[0]][curr_pipe[1]]]:
                r, c = dir
                adc_r, adj_c = r+curr_pipe[0], c+curr_pipe[1]

                if adc_r not in range(len(grid)) or adj_c not in range(len(grid[0])):
                    continue
                
                if grid[adc_r][adj_c] == 'S' and len(visited) > 2:
                    next_pipe = None
                    break
                
                if grid[adc_r][adj_c] in connecting[(r, c)] and (adc_r, adj_c) not in visited:
                    next_pipe = (adc_r, adj_c)
                    visited.add((adc_r, adj_c))
                    steps += 1
                    break

        print(steps//2 + 1)

part_a()