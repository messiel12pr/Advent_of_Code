def calculate_min_hold_time(time, distance):
    for i in range(time):
        if (time - i) * i > distance:
            return i
        
    return 0

def part_a():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        times = input[0].split(': ')[1].strip().split(' ')
        distances = input[1].split(': ')[1].strip().split(' ')
        total_wins = 1
 
        while times and distances:
            if not times[0].isdigit():
                times.pop(0)

            if not distances[0].isdigit():
                distances.pop(0)

            if times[0].isdigit() and distances[0].isdigit():
                curr_time = int(times.pop(0))
                curr_distance = int(distances.pop(0))
                min_hold_time = calculate_min_hold_time(curr_time, curr_distance)
                max_hold_time = curr_time - min_hold_time
                total_wins *=  max_hold_time - min_hold_time + 1
        
        print(total_wins)





part_a()