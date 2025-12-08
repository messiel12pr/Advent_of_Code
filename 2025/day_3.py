import sys

def part_1():
    line = list(map(int, sys.stdin.readline().strip()))
    total_jolt = 0

    while line:
        a = max(line)
        a_idx = line.index(a)
        b, c = 0, 0

        if a_idx != 0:
            b = max(line[:a_idx]) * 10 + a

        if a_idx != len(line) - 1:
            c = a * 10 + max(line[a_idx+1:])

        total_jolt += max(b, c)
        line = list(map(int, sys.stdin.readline().strip()))
    return total_jolt

#print(part_1())

# incomplete
def part_2():
    line = list(map(int, sys.stdin.readline().strip()))
    total_jolt = 0

    while line:
        ctr = 0
        turned_on = [0] * len(line)

        for i in range(9, 0, -1):
            if ctr == 12:
                break

            for j in range(len(line)):
                if ctr == 12:
                    break

                if line[j] == i and not turned_on[j]:
                    turned_on[j] = 1
                    ctr += 1

        ctr = 0
        turned_on_reversed = [0] * len(line)
        for i in range(9, 0, -1):
            if ctr == 12:
                break

            for j in range(len(line)-1, -1, -1):
                if ctr == 12:
                    break

                if line[j] == i and not turned_on_reversed[j]:
                    turned_on_reversed[j] = 1
                    ctr += 1
        
        print(turned_on)
        print(turned_on_reversed)
        print()

        #total_jolt += 
        line = list(map(int, sys.stdin.readline().strip()))
    return total_jolt

print(part_2())