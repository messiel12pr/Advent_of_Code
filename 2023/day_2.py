def get_number(curr_line: str):
    number = curr_line.strip()
    if not number[-1].isdigit():
        number = number[:-1]
    return int(number)


def get_color(curr_line: str):
    color = curr_line.strip()
    if not color[-1].isalpha():
        color = color[:-1]
    return color


def part_1():
    with open('input.txt', 'r') as file:
        total = 0
        line = file.readline()

        while line:
            games = {}
            id = get_number(line[5:8])
            i = len(str(id)) + 7
            while i < len(line):
                if line[i].isdigit():
                    number = get_number(line[i:i+3])
                    curr_index = len(str(number)) + i + 1
                    color = get_color(line[curr_index:curr_index+5])

                    if color not in games:
                        games[color] = number
                    else:
                        games[color] = max(games[color], number)

                    i = curr_index + len(color)

                else:
                    i += 1

            red = games['red'] - 12
            green = games['green'] - 13
            blue = games['blue'] - 14

            if red < 1 and green < 1 and blue < 1:
                total += id

            line = file.readline()
        print(total)


def part_2():
    with open('input.txt', 'r') as file:
        total = 0
        line = file.readline()

        while line:
            games = {}
            id = get_number(line[5:8])
            i = len(str(id)) + 7
            while i < len(line):
                if line[i].isdigit():
                    number = get_number(line[i:i+3])
                    curr_index = len(str(number)) + i + 1
                    color = get_color(line[curr_index:curr_index+5])

                    if color not in games:
                        games[color] = number
                    else:
                        games[color] = max(games[color], number)

                    i = curr_index + len(color)

                else:
                    i += 1

            total += games['red'] * games['green'] * games['blue']

            line = file.readline()
        print(total)


part_1()
part_2()
