
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


def calculate_depth_card(depth_cards, cards_matching_nums, card):
    stack = [card]

    counter = 0
    while stack:
        curr_card = stack.pop()

        if curr_card in depth_cards:
            counter += depth_cards[curr_card]

        else:
            for i in range(1, cards_matching_nums[curr_card] + 1):
                if curr_card + i in cards_matching_nums:
                    stack.append(curr_card + i)
                    counter += 1

    depth_cards[card] = counter
    return counter


def calculate_total_cards(cards_matching_nums):
    depth_cards = {}
    total_depth = 0
    for i in range(len(cards_matching_nums), 0, -1):
        total_depth += calculate_depth_card(
            depth_cards, cards_matching_nums, i)

    return total_depth + len(cards_matching_nums)


def part_b():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        cards_matching_nums = {}

        for i, line in enumerate(input, 1):
            nums, winning_nums = line.split(': ')[1].split(' | ')
            nums = nums.split(' ')
            winning_nums = winning_nums.split(' ')

            matching_nums = 0
            for num in nums:
                if num != '' and num in winning_nums:
                    matching_nums += 1

            cards_matching_nums[i] = matching_nums

        print(calculate_total_cards(cards_matching_nums))


part_b()
