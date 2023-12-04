
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


part_a()
