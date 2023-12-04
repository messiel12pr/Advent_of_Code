
import time


def part_a():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        total_points = 0

        for line in input:
            nums, winning_nums = line.split(': ')[1].split(' | ')
            nums = nums.split(' ')
            winning_nums = winning_nums.split(' ')

            points = 0
            for num in nums:
                if num != '' and num in winning_nums and points != 0:
                    points += points

                elif num != '' and num in winning_nums and points == 0:
                    points = 1

            total_points += points

    print(total_points)


def calculate_depth_scratchcard(depths_map, map, card):
    stack = [card]

    counter = 0
    while stack:
        curr_card = stack.pop()

        if curr_card in depths_map:
            counter += depths_map[curr_card]
        else:
            for i in range(1, map[curr_card] + 1):
                if curr_card + i in map:
                    stack.append(curr_card + i)
                    counter += 1

    depths_map[card] = counter
    return counter


def calculate_total_scratchcards(scratchcards_values):
    depths_map = {}
    total_depth = 0
    for i in scratchcards_values:
        total_depth += calculate_depth_scratchcard(
            depths_map, scratchcards_values, i)
    return total_depth + len(scratchcards_values)


def part_b():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        scratchcards_values = {}

        for i, line in enumerate(input, 1):
            nums, winning_nums = line.split(': ')[1].split(' | ')
            nums = nums.split(' ')
            winning_nums = winning_nums.split(' ')

            matching_nums = 0
            for num in nums:
                if num != '' and num in winning_nums:
                    matching_nums += 1

            scratchcards_values[i] = matching_nums

        print(calculate_total_scratchcards(scratchcards_values))


part_b()
