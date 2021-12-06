import numpy as np

with open('input', 'r') as input_file:
    input = input_file.read().strip()
    lantern_fishes = []


    TICKS = 256

    lantern_fishes = np.array(input.split(','), dtype=int)
    lantern_fishes_map = {}

    for i in range(9):
        lantern_fishes_map[i] = int(np.count_nonzero(lantern_fishes == i))

    print(','.join(map(lambda x: str(x), lantern_fishes_map.values())))

    for day in range(TICKS):
        print(f'Processing day {day}')

        value_for_next_i = None

        for i in reversed(range(1, 9)):
            if i - 1 == 0:
                lantern_fishes_map[8] += lantern_fishes_map[i - 1]
                lantern_fishes_map[6] += lantern_fishes_map[i - 1]

            if value_for_next_i is not None:
                temp_value = value_for_next_i
            else:
                temp_value = lantern_fishes_map[i]
                lantern_fishes_map[i] = 0
            value_for_next_i = lantern_fishes_map[i - 1]
            lantern_fishes_map[i - 1] = temp_value
        
        print(f'After day {day + 1}\t', ','.join(map(lambda x: str(x), lantern_fishes_map.values())))

    print(f'Total fishes: {sum(lantern_fishes_map.values())}')
