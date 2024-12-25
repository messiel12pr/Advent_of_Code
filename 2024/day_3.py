line = input()

def part_1():
    res = 0
    i = 0
    while i < len(line):
        num1 = []
        num2 = []
        if line[i:i+4] != 'mul(':    
            i += 1
            continue

        i += 4
        while i < len(line):
            if not line[i].isdigit():
                break

            num1.append(line[i])
            i += 1

        if line[i] != ',':
            continue
        i += 1

        while i < len(line):
            if not line[i].isdigit():
                break

            num2.append(line[i])
            i += 1

        if line[i] != ')':
            continue
        i += 1

        res += int(''.join(num1)) * int(''.join(num2))

    print(res)


def part_2():
    res = 0
    i = 0
    while i < len(line):
        num1 = []
        num2 = []
        if line[i:i+7] == "don't()":
            while i < len(line) and line[i:i+4] != 'do()':
                i += 1

        if line[i:i+4] != 'mul(':    
            i += 1
            continue

        i += 4
        while i < len(line):
            if not line[i].isdigit():
                break

            num1.append(line[i])
            i += 1

        if line[i] != ',':
            continue
        i += 1

        while i < len(line):
            if not line[i].isdigit():
                break

            num2.append(line[i])
            i += 1

        if line[i] != ')':
            continue
        i += 1

        res += int(''.join(num1)) * int(''.join(num2))

    print(res)

part_1()
part_2()