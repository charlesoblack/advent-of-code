#! /usr/bin/env python3


def get_wire_locations(instructions):
    instructions = instructions.split(',')

    current_loc = [0, 0]
    locations = []

    for instruction in instructions:
        direction = instruction[0]
        length = int(instruction[1:])

        if direction in ('U', 'D'):
            idx = 1
        elif direction in ('L', 'R'):
            idx = 0

        if direction in ('D', 'L'):
            mult = -1
        elif direction in ('U', 'R'):
            mult = 1

        for n in range(length):
            current_loc[idx] += mult
            locations.append(tuple(current_loc))

    return locations


with open('03-input.txt', 'r') as f:
    wires = f.readlines()

# sample inputs
# wires = ['R8,U5,L5,D3',
#          'U7,R6,D4,L4']  # 6
# wires = ['R75,D30,R83,U83,L12,D49,R71,U7,L72',
#          'U62,R66,U55,R34,D71,R55,D58,R83']  # 159
# wires = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
#          'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']  # 135


first_wire_locs = get_wire_locations(wires[0])
second_wire_locs = get_wire_locations(wires[1])

common_locs = set(first_wire_locs) & set(second_wire_locs)

closest_locs = sorted(list(common_locs), key=lambda x: abs(x[0]) + abs(x[1]))

print('closest location: {}'.format(closest_locs[0]))
print('manhattan distance: {}'.format(sum([abs(x) for x in closest_locs[0]])))
