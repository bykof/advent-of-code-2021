from os import stat
import typing


class Crab:
    def __init__(self, position: int) -> None:
        self.position = position

    def costs_for_move(self, new_position: int) -> int:
        return abs(new_position - self.position)

class CrabReader:
    @staticmethod
    def read_crabs() -> typing.List[Crab]:
        with open('input', 'r') as input_file:
            return list(map(lambda x: Crab(int(x)), input_file.read().strip().split(',')))
    

crabs = CrabReader.read_crabs()
highest_position = None
lowest_position = None

for crab in crabs:
    if highest_position is None:
        highest_position = crab.position
        continue

    if lowest_position is None:
        lowest_position = crab.position
        continue

    if highest_position < crab.position:
        highest_position = crab.position
    if lowest_position > crab.position:
        lowest_position = crab.position

costs = {}

for i in range(lowest_position, highest_position + 1):
    for crab in crabs:
        
        if i not in costs:
            costs[i] = 0

        costs[i] += crab.costs_for_move(i)
    
min_value = min(costs.values())
min_index = list(costs.values()).index(min_value)

print(f'Horizontal Position: {min_index}, with fuel: {min_value}')


    

