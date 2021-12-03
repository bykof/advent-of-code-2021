import typing

HIGH_BIT = '1'
LOW_BIT = '0'

def rates(bits: typing.List[typing.List[str]]):
    if len(bits) <= 0:
        raise Exception('please specify an input with at least one line')

    gamma_rate = ''
    epsilon_rate = ''
    bits_per_line = len(bits[0])

    for x in range(bits_per_line):
        high_bits_counter = 0
        low_bits_counter = 0
        bit_lines = len(bits)

        for y in range(bit_lines):
            bit = bits[y][x]
            if bit == HIGH_BIT:
                high_bits_counter += 1
            elif bit == LOW_BIT:
                low_bits_counter += 1
            else:
                raise Exception(f'Some strange input was given as bit: Input({bit})')
            
            if high_bits_counter > bit_lines / 2:
                gamma_rate += '1'
                epsilon_rate += '0'
                break
            if low_bits_counter > bit_lines / 2:
                gamma_rate += '0'
                epsilon_rate += '1'
                break  
    return int(gamma_rate, 2), int(epsilon_rate, 2)

with open('input', 'r') as input_file:
    lines = input_file.readlines()
    bits = [list(line.strip()) for line in lines]
    temp_gamma_rate, temp_epsilon_rate = rates(bits)
    power_consumption = temp_epsilon_rate * temp_gamma_rate
    print(f'Power Consumption: {power_consumption}')
