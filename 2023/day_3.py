symbols = ['@', '=', '&', '*', '%', '$', '-', '+', '#', '/']


def adjacent_to_symbol(matrix, r, c):
    adjacent = [[0, 1], [0, -1], [1, 0], [-1, 0],
                [1, 1], [1, -1], [-1, 1], [-1, -1]]
    rows = len(matrix)
    columns = len(matrix[0])

    for r1, c2 in adjacent:
        curr_r, curr_c = r1 + r, c2 + c
        if curr_r in range(rows) and curr_c in range(columns) and matrix[curr_r][curr_c] in symbols:
            return True

    return False


def part_a():
    with open('input.txt', 'r') as file:
        input = file.read()
        matrix = []
        total_sum = 0

        for line in input.split('\n'):
            matrix.append(line)

        for i in range(len(matrix)):
            number = ''
            j = 0
            while j < len(matrix[0]):
                if matrix[i][j].isdigit() and adjacent_to_symbol(matrix, i, j):
                    sub_str = matrix[i]
                    while j in range(len(sub_str)) and sub_str[j] != '.' and sub_str[j] not in symbols:
                        number += matrix[i][j]
                        j += 1

                    total_sum += int(number)
                    number = ''

                elif matrix[i][j].isdigit():
                    number += matrix[i][j]

                else:
                    number = ''

                j += 1

        print(total_sum)


def extract_number(sub_list, curr_index):
    num = sub_list[curr_index]
    l = curr_index - 1
    r = curr_index + 1

    while l >= 0 and sub_list[l].isdigit():
        num = sub_list[l] + num
        l -= 1

    while r < len(sub_list) and sub_list[r].isdigit():
        num = num + sub_list[r]
        r += 1

    return int(num)


def adjacent_part_numbers(matrix, r, c):
    adjacent = [[0, 1], [0, -1], [1, 0], [-1, 0],
                [1, 1], [1, -1], [-1, 1], [-1, -1]]
    rows = len(matrix)
    columns = len(matrix[0])
    visited = set()

    adjacent_numbers = []
    for r1, c2 in adjacent:
        curr_r, curr_c = r1 + r, c2 + c
        if curr_r in range(rows) and curr_c in range(columns) and matrix[curr_r][curr_c].isdigit():
            num = extract_number(matrix[curr_r][:], curr_c)
            if num not in visited:
                visited.add(num)
                adjacent_numbers.append(num)

    return adjacent_numbers


def part_b():
    with open('input.txt', 'r') as file:
        input = file.read()
        matrix = []
        total_sum = 0

        for line in input.split('\n'):
            matrix.append(line)

        for i in range(len(matrix)):
            number = ''
            j = 0
            while j < len(matrix[0]):
                if matrix[i][j] == '*':
                    adj_nums = adjacent_part_numbers(matrix, i, j)
                    if adj_nums and len(adj_nums) == 2:
                        total_sum += adj_nums[0] * adj_nums[1]

                    number = ''

                j += 1

        print(total_sum)


part_a()
part_b()
