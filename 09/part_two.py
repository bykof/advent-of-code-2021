def find_basin_count(lines, index, count=0, passed=[]):
    y, x = index

    if index in passed:
        return count

    passed.append(index)
    value = lines[y][x]

    if value == 9:
        return count

    count += 1
    right_value = lines[y][x+1] if x + 1 < len(lines[y]) else None
    left_value = lines[y][x-1] if x - 1 >= 0 else None
    bottom_value = lines[y+1][x] if y + 1 < len(lines) else None
    top_value = lines[y-1][x] if y - 1 >= 0 else None

    if right_value is not None:
        count = find_basin_count(lines, (y, x+1), count, passed)

    if left_value is not None:
        count = find_basin_count(lines, (y, x-1), count, passed)

    if top_value is not None:
        count = find_basin_count(lines, (y-1, x), count, passed)

    if bottom_value is not None:
        count = find_basin_count(lines, (y+1, x), count, passed)

    return count


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

    sum_lowest_basin_counts = 1
    basin_counts = []
    
    for lowest_index in lowest_indices:
        basin_count = find_basin_count(lines, lowest_index)
        basin_counts.append(basin_count)
    sorted_basin_counts = sorted(basin_counts)
    multiplied_last_three_baisin = 1
    
    for baisin in sorted_basin_counts[-3:]:
        multiplied_last_three_baisin *= baisin
    
    print(multiplied_last_three_baisin)
