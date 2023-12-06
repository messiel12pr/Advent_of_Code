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


def part_b(input_filename):
    with open(input_filename, 'r') as file:
        input = file.read()
        seeds = list(map(int, input.splitlines()[0].split(': ')[1].split(' ')))
        input = input.splitlines()[2:]
        lowest_location = sys.maxsize

        for i in range(0, len(seeds), 2):
            for seed in range(seeds[i], seeds[i] + seeds[i+1], 1):
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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day_5.py input.txt")
        sys.exit(1)

    input_filename = sys.argv[1]
    part_b(input_filename)