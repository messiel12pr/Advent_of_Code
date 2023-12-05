import sys


def part_a():
    with open('input.txt', 'r') as file:
        input = file.read()
        seeds = map(int, input.splitlines()[0].split(': ')[1].split(' '))
        input = input.splitlines()[2:]
        lowest_location = sys.maxsize

        for seed in seeds:
            source_number = seed
            flag = False
            for line in input:
                if flag and not line:
                    flag = False

                if flag or not line or line and not line[0].isdigit():
                    continue

                destination_range_start, source_range_start, length_range = map(
                    int, line.split(' '))

                source_range_end = source_range_start + length_range

                if source_number in range(source_range_start, source_range_end):
                    source_number = source_number - source_range_start + destination_range_start
                    flag = True

            lowest_location = min(lowest_location, source_number)

        print(lowest_location)


part_a()
