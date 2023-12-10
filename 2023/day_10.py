
from functools import reduce

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
        stack = [start]
        steps = 0

        while stack:
            curr_pipe = stack.pop()
            
            for dir in directions[grid[curr_pipe[0]][curr_pipe[1]]]:
                r, c = dir

                if r+curr_pipe[0] not in range(len(grid)) or c+curr_pipe[1] not in range(len(grid[0])):
                    continue
                
                if grid[r+curr_pipe[0]][c+curr_pipe[1]] == 'S' and len(visited) > 2:
                    stack.clear()
                    break
                
                if grid[r+curr_pipe[0]][c+curr_pipe[1]] in connecting[(r, c)] and (r+curr_pipe[0], c+curr_pipe[1]) not in visited:
                    stack.append((r+curr_pipe[0], c+curr_pipe[1]))
                    visited.add((r+curr_pipe[0], c+curr_pipe[1]))
                    steps += 1
                    break

        print(steps//2 + 1)

part_a()