from collections import defaultdict
import sys

# Nothing fishy around here -_-
new_recursion_limit = 3000
sys.setrecursionlimit(new_recursion_limit)

def part_a():
    with open('input.txt', 'r') as file:
        grid = [list(x) for x in file.read().splitlines()]
        coords = {
                    '|':  [(-1, 0), (1, 0)],
                    '-':  [(0, -1), (0, 1)],
                    '/':  [(-1, 0), (1, 0), (0, 1), (0, -1)],
                    '\\': [(1, 0), (-1, 0), (0, -1), (0, 1)]
                 }
        
        iterated = defaultdict(list)

        def path_rec(curr_coord: tuple, dir: tuple):
            x, y = dir[0] + curr_coord[0], dir[1] + curr_coord[1]

            if x not in range(len(grid)) or y not in range(len(grid[0])):
                return
            
            if (x, y) in iterated and dir in iterated[(x, y)]:
                return
            
            else:
                iterated[(x, y)].append(dir)

            if (grid[x][y] == '.')  or \
                    (grid[x][y] == '|' and (dir == (-1, 0) or dir == (1, 0))) or \
                    (grid[x][y] == '-' and (dir == (0, -1) or dir == (0, 1))):
                
                path_rec((x, y), dir)
            
            elif grid[x][y] == '|' or grid[x][y] == '-':
                dir_1 = coords[grid[x][y]][0]
                dir_2 = coords[grid[x][y]][1]
                path_rec((x, y), dir_1)
                path_rec((x, y), dir_2)

            elif grid[x][y] == '/' or grid[x][y] == '\\':
                if dir == (0, 1):
                    dir = coords[grid[x][y]][0]

                elif dir == (0, -1):
                    dir = coords[grid[x][y]][1]

                elif dir == (-1, 0):
                    dir = coords[grid[x][y]][2]

                else:
                    dir = coords[grid[x][y]][3]

                path_rec((x, y), dir)
        
        path_rec((0, -1), (0, 1))
        print(len(iterated))

part_a()