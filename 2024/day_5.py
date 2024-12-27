from collections import defaultdict
import sys
data = sys.stdin.read().splitlines()
idx = data.index('')
rules, updates = data[:idx], data[idx + 1:]
ordering = defaultdict(list)

for rule in rules:
    first, second = rule.split('|')
    ordering[first].append(second)

def part_1():
    res = 0
    for update in updates:
        seen = set()
        new_update = update.split(',')
        for num in new_update:
            if num in ordering:
                flag = False
                for second in ordering[num]:
                    if second in seen:
                        flag = True
                        break
                if flag:
                    break
            seen.add(num)

        if len(seen) == len(new_update):
            res += int(new_update[len(new_update)//2])

    print(res)

part_1()