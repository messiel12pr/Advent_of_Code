
'''
    get ascii
    increase current value by ascii
    multiply by 17
    remainder 256
'''

def part_a():
    with open('input.txt', 'r') as file:
        input = file.read().split(',')
        total = 0

        for line in input:
            current = 0
            for ch in line:
                current += ord(ch)
                current = (current * 17) % 256
            total += current

        print(total)
part_a()