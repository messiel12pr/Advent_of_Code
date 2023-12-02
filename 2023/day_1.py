
with open('input.txt', 'r') as file:
    total_sum = 0
    line = file.readline()

    while line:
        l = 0
        r = len(line) - 2

        while l < len(line) - 2:
            if line[l].isdigit():
                break
            l += 1

        while r > 0:
            if line[r].isdigit():
                break
            r -= 1

        total_sum += int(line[l] + line[r])
        line = file.readline()

    print(total_sum)
