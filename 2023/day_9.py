
def part_a():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        total_sum = 0

        for line in input:
            line = list(map(int, line.split()))
            matrix = []
            matrix.append(line)

            while True:
                row = []
                ctr = 0

                for idx in range(len(line) - 1):
                    row.append(line[idx + 1] - line[idx])
                    if line[idx + 1] - line[idx] == 0:
                        ctr += 1

                line = row
                matrix.append(row)

                if ctr == len(row):
                    break

            for row in range(len(matrix)):
                total_sum += matrix[row][-1]

        print(total_sum)

part_a()