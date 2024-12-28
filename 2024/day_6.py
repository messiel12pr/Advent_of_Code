import sys
data = sys.stdin.read().splitlines()

# right, down, left, up
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def next_direction():
    while True:
        for dir in directions:
            yield dir

next_dir = next_direction()

def search(r, c):
    visited = set()
    direction = (-1, 0)

    while True:
        if r not in range(len(data)) or c not in range(len(data[0])):
            break

        if data[r][c] == '#':
            r -= direction[0]
            c -= direction[1]
            direction = next(next_dir)

        visited.add((r, c))
        r += direction[0]
        c += direction[1]

    return len(visited)

def part_1():
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == '^':
                return search(r, c)
            
print(part_1())