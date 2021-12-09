with open('input', 'r') as input_file:
    lines = [
        [
            int(number)
            for number in line
        ]
        for line in input_file.read().strip().split('\n')
    ]
    lowest_indices = []
    sum_lowest = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            value = lines[y][x]
            right_value = lines[y][x+1] if x + 1 < len(lines[y]) else None
            left_value = lines[y][x-1] if x - 1 > -1 else None
            bottom_value = lines[y+1][x] if y + 1 < len(lines) else None
            top_value = lines[y-1][x] if y - 1 > -1 else None
            
            conditions = []
            if right_value is not None:
                conditions.append(value < right_value)

            if left_value is not None:
                conditions.append(value < left_value)
            
            if top_value is not None:
                conditions.append(value < top_value)

            if bottom_value is not None:
                conditions.append(value < bottom_value)

            if all(conditions):
                lowest_indices.append((y, x))
                sum_lowest += value + 1

    print(sum_lowest)


            