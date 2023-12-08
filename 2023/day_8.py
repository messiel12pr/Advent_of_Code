def part_a():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        instructions = list(input[0])
        document_map = {}
        steps = 0

        for idx, instruction in enumerate(instructions):
            if instruction == 'L':
                instructions[idx] = 0

            else:
                instructions[idx] = 1

        for line in input[2:]:
            key, value = line.split(' = ')
            value = value[1:-1]
            l, r = value.split(', ')
            document_map[key] = (l, r)

        found = False
        curr_node = 'AAA'
        while not found:
            for dir in instructions:
                curr_node = document_map[curr_node][dir]
                steps += 1

                if curr_node == 'ZZZ':
                    found = True
                    break

        print(steps)

#part_a()

def part_b():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        instructions = list(input[0])
        document_map = {}
        starting_nodes = []

        for idx, instruction in enumerate(instructions):
            if instruction == 'L':
                instructions[idx] = 0

            else:
                instructions[idx] = 1

        for line in input[2:]:
            key, value = line.split(' = ')
            value = value[1:-1]
            l, r = value.split(', ')
            document_map[key] = (l, r)

            if key[2] == 'A':
                starting_nodes.append(key)

        
        found = False
        z_count = 0
        steps = 0
        
        while not found:
            for dir in instructions:
                if found:
                    break
                
                steps += 1
                for idx, node in enumerate(starting_nodes):                    
                    curr_node = document_map[node][dir]
                    starting_nodes[idx] = curr_node

                    if node[2] == 'Z' and curr_node[2] != 'Z':
                        z_count -= 1

                    if node[2] != 'Z' and curr_node[2] == 'Z':
                        z_count += 1

                if z_count == len(starting_nodes):
                        found = True
                        break

        print(steps)

part_b()