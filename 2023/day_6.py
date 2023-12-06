def calculate_min_hold_time(time, distance):
    for i in range(time):
        if (time - i) * i > distance:
            return i
        
    return 0

def part_a():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        times = list(map(int, input[0].split(': ')[1].strip().split()))
        distances = list(map(int, input[1].split(': ')[1].strip().split()))
        total_wins = 1

        for i in range(len(times)):
            min_hold_time = calculate_min_hold_time(times[i], distances[i])
            max_hold_time = times[i] - min_hold_time
            total_wins *=  max_hold_time - min_hold_time + 1
        
        print(total_wins)



part_a()