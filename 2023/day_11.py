
def part_a():
    with open('input.txt', 'r') as file:
        input = list(map(list, file.read().splitlines()))
        columns =  {}
        rows = {}
        galaxies = {}
        ctr = 1

        for r in range(len(input)):
            for c in range(len(input[0])):
                if input[r][c] == '#':
                    galaxies[ctr] = (r, c)
                    input[r][c] = ctr
                    ctr += 1

                if input[r][c] == '.':
                    rows[r] = rows.get(r, 0) + 1

                if input[r][c] == '.':
                    columns[c] = columns.get(c, 0) + 1

        for row, cnt in reversed(rows.items()):
            if cnt == len(input):
                for galaxy, coord in galaxies.items():
                    if coord[0] > row:
                        galaxies[galaxy] = (coord[0] + 1, coord[1])
        
        for col, cnt in reversed(columns.items()):
            if cnt == len(input[0]):
                for galaxy, coord in galaxies.items():
                    if coord[1] > col:
                        galaxies[galaxy] = (coord[0], coord[1] + 1)

        total_sum = 0
        coords = list(galaxies.values())

        for i in range(len(coords)):
            x1, y1 = coords[i]
            for j in range(i + 1, len(coords), 1):
                x2, y2 = coords[j]
                total_sum += abs(x1 - x2) + abs(y1 - y2)

        print(total_sum)

part_a()