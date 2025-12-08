from collections import defaultdict
import sys, math

# Reused class from my comp programming course at uni :)
class Disjoint():
    def __init__(self, n):
        self.set = [-1 for _ in range(n)]
        self.connected = False

    def union(self, a, b):
        root_a = self.find_set(a)
        root_b = self.find_set(b)
        # Already in the same component
        if root_a == root_b:
            return
        
        if self.set[root_a] <= self.set[root_b]:
            # Update size of component
            self.set[root_a] += self.set[root_b]
            # Make smaller component part of bigger component
            self.set[root_b] = root_a
        
        else:
            self.set[root_b] += self.set[root_a]
            self.set[root_a] = root_b

        if abs(self.set[root_a]) == len(self.set) or abs(self.set[root_b]) == len(self.set):
            self.connected = True

    def find_set(self, a):
        if self.set[a] < 0:
            return a
        
        # path compression (make all of the nodes in a component point to their root)
        self.set[a] = self.find_set(self.set[a])
        return self.set[a]
    
    def three_largest(self):
        a, b, c = map(abs, sorted(self.set)[0:3])
        return a * b * c
    
    def all_connected(self):
        return self.connected


def part_1():
    lines = sys.stdin.readlines()
    junctions = []
    junction_pos = defaultdict(int)
    for i, line in enumerate(lines):
        x, y, z = map(int, line.strip().split(','))
        junctions.append((x, y, z))
        junction_pos[(x, y, z)] = i

    distances = []
    for i, junction in enumerate(junctions):
        for j in range(i+1, len(junctions)):
            distances.append((math.dist(junction, junctions[j]), junction, junctions[j]))

    distances = sorted(distances)
    disjoint = Disjoint(len(junctions))
    for i in range(len(distances)):
        distance, junction_1, junction_2 = distances[i]
        if i == 1000:
            break
        disjoint.union(junction_pos[junction_1], junction_pos[junction_2])

    return disjoint.three_largest()

#print(part_1())


def part_2():
    lines = sys.stdin.readlines()
    junctions = []
    junction_pos = defaultdict(int)
    for i, line in enumerate(lines):
        x, y, z = map(int, line.strip().split(','))
        junctions.append((x, y, z))
        junction_pos[(x, y, z)] = i

    distances = []
    for i, junction in enumerate(junctions):
        for j in range(i+1, len(junctions)):
            distances.append((math.dist(junction, junctions[j]), junction, junctions[j]))

    distances = sorted(distances)
    disjoint = Disjoint(len(junctions))
    junction_1, junction_2 = 0, 0
    for i in range(len(distances)):
        distance, junction_1, junction_2 = distances[i]
        disjoint.union(junction_pos[junction_1], junction_pos[junction_2])
        if disjoint.all_connected():
            return junction_1[0] * junction_2[0]
    return junction_1[0] * junction_2[0]

print(part_2())