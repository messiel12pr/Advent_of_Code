symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*',
                '(', ')', '-', '_', '=', '+', '[', ']',
                '{', '}', '|', ';', ':', "'", '"', ',',
                '<', '>', '/', '?', '`', '~']


def adjacent_to_symbol(matrix, r, c):
    adjacent = [[0, 1], [0, -1], [1, 0], [-1, 0],
                [1, 1], [1, -1], [-1, 1], [-1, -1]]
    rows = len(matrix)
    columns = len(matrix[0])

    for r1, c2 in adjacent:
        curr_r, curr_c = r1 + r, c2 + c
        if curr_r in range(rows) and curr_c in range(columns) and matrix[curr_r][curr_c] in symbols_list:
            return True

    return False


with open('input.txt', 'r') as file:
    input = file.read()
    lines = input.split('\n')
    matrix = []
    total_sum = 0

    for line in lines:
        matrix.append(line)

    for i in range(len(matrix)):
        number = ''
        j = 0
        while j < len(matrix[0]):
            if matrix[i][j].isdigit() and adjacent_to_symbol(matrix, i, j):
                sub_str = matrix[i]
                while j in range(len(sub_str)) and sub_str[j] != '.' and sub_str[j] not in symbols_list:
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
