from functools import reduce
import pprint as p

def part_a():
    with open('input.txt', 'r') as file:
        grid = [x for x in file.read().split('\n')]
        total_load = 0

        for col in range(len(grid[0])):
            column_list = []
            for row in range(len(grid)):
                column_list.append(grid[row][col])

            count_zeroes = 0

            for idx in range(len(column_list) - 1, -1, -1):
                count_zeroes += 1 if column_list[idx] == 'O' else 0

                if column_list[idx] == '#' and count_zeroes > 0:
                    i = idx + 1
                    while count_zeroes != 0:
                        total_load += len(column_list[i:])
                        count_zeroes -= 1
                        i += 1
            
            if count_zeroes > 0:
                i = 0
                while count_zeroes != 0:
                    if column_list[i] != '#':
                        total_load += len(column_list[i:])
                        count_zeroes -= 1
                    i += 1 
                    
        print(total_load)

part_a()