import sys
from collections import Counter

data = sys.stdin.read().splitlines()
ls1, ls2 = [], []

for line in data:
    d1, d2 = map(int, line.split('   '))
    ls1.append(d1)
    ls2.append(d2)

ls1.sort()
ls2.sort()

def part_1():
    res = 0
    for i in range(len(ls1)):
        res += abs(ls1[i] - ls2[i])
    print(res)

def part_2():
    res = 0
    hm = Counter(ls2)
    for i in range(len(ls1)):
        res += ls1[i] * hm[ls1[i]] 
    print(res)

part_1()
part_2()