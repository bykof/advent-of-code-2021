from os import terminal_size
import typing

HIGH_BIT = '1'
LOW_BIT = '0'


def filter_by_bit_at_index(bits: typing.List[typing.List[str]], bit: str, index: int) -> typing.List[typing.List[str]]:
    return [
        bit_line
        for bit_line in bits
        if bit_line[index] == bit
    ]


def oxygen_generator_rating(bits: typing.List[typing.List[str]]):
    if len(bits) <= 0:
        raise Exception('please specify an input with at least one line')

    current_index = -1
    oxygen_generator_bits = bits.copy()
    

    while len(oxygen_generator_bits) != 1:
        current_index += 1
        oxygen_generator_zipped_bits = [map(lambda x: int(x), line) for line in list(zip(*oxygen_generator_bits))]
        oxygen_generator_zipped_bits_line = list(oxygen_generator_zipped_bits[current_index])
        zipped_bits_sum = sum(oxygen_generator_zipped_bits_line)
        
        if zipped_bits_sum > len(oxygen_generator_zipped_bits_line) / 2:
            oxygen_generator_bits = filter_by_bit_at_index(
                oxygen_generator_bits,
                HIGH_BIT,
                current_index,
            )
        elif zipped_bits_sum < len(oxygen_generator_zipped_bits_line) / 2:
            oxygen_generator_bits = filter_by_bit_at_index(
                oxygen_generator_bits,
                LOW_BIT,
                current_index,
            )
        else:
            oxygen_generator_bits = filter_by_bit_at_index(
                oxygen_generator_bits,
                HIGH_BIT,
                current_index,
            )
        
    return int(''.join(oxygen_generator_bits[0]), 2)

def co2_scrubber_generator_rating(bits: typing.List[typing.List[str]]):
    if len(bits) <= 0:
        raise Exception('please specify an input with at least one line')

    current_index = -1
    co2_scrubber_generator_bits = bits.copy()
    

    while len(co2_scrubber_generator_bits) != 1:
        current_index += 1
        co2_scrubber_generator_zipped_bits = [map(lambda x: int(x), line) for line in list(zip(*co2_scrubber_generator_bits))]
        co2_scrubber_generator_zipped_bits_line = list(co2_scrubber_generator_zipped_bits[current_index])
        zipped_bits_sum = sum(co2_scrubber_generator_zipped_bits_line)
        
        if zipped_bits_sum > len(co2_scrubber_generator_zipped_bits_line) / 2:
            co2_scrubber_generator_bits = filter_by_bit_at_index(
                co2_scrubber_generator_bits,
                LOW_BIT,
                current_index,
            )
        elif zipped_bits_sum < len(co2_scrubber_generator_zipped_bits_line) / 2:
            co2_scrubber_generator_bits = filter_by_bit_at_index(
                co2_scrubber_generator_bits,
                HIGH_BIT,
                current_index,
            )
        else:
            co2_scrubber_generator_bits = filter_by_bit_at_index(
                co2_scrubber_generator_bits,
                LOW_BIT,
                current_index,
            )
        
    return int(''.join(co2_scrubber_generator_bits[0]), 2)

with open('input', 'r') as input_file:
    lines = input_file.readlines()
    bits = [list(line.strip()) for line in lines]
    temp_oxygen_generator_rating = oxygen_generator_rating(bits)
    temp_co2_scrubber_generator_rating = co2_scrubber_generator_rating(bits)
    print(f'Oxygen Generator Rating: {temp_oxygen_generator_rating}')
    print(f'CO2 Scrubber Generator Rating: {temp_co2_scrubber_generator_rating}')
    print(f'Life Support Rating: {temp_co2_scrubber_generator_rating * temp_oxygen_generator_rating}')
