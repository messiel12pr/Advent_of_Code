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
        l = 0
        r = len(line) - 1
        turned_on = [False] * len(line)

        while l < r and ctr != 12:
            if line[l] > line[r]:
                turned_on[l] = True
                l += 1
                ctr += 1

            elif line[r] > line[l]:
                turned_on[r] = True
                r -= 1
                ctr += 1

            else:
                l += 1
                r -= 1

        curr_jolt = []
        for i in range(len(turned_on)):
            if turned_on[i]:
                curr_jolt.append(line[i])

            else:
                curr_jolt.append(0)

        #total_jolt += 
        line = list(map(int, sys.stdin.readline().strip()))
    return total_jolt

print(part_2())