import typing


class LanternFish:
    def __init__(self, timer=8) -> None:
        self.timer = timer

    def tick(self) -> typing.Optional['LanternFish']:
        
        if self.timer == 0:
            self.timer = 6
            return LanternFish()
        
        self.timer -= 1
        return

    def __str__(self) -> str:
        return f'{self.timer}'    


with open('input', 'r') as input_file:
    input_lines = input_file.read().strip().split('\n')
    lantern_fishes = []
    
    TICKS = 80
        
    for timer in input_lines[0].split(','):
        lantern_fishes.append(LanternFish(int(timer)))
    
    # print(f'Initial State', ','.join([str(f) for f in lantern_fishes]))
    for day in range(TICKS):   
        new_lantern_fishes = []     
        
        for lantern_fish in lantern_fishes:
            new_lantern_fish = lantern_fish.tick()
            
            if new_lantern_fish:
                new_lantern_fishes.append(new_lantern_fish)
                
        lantern_fishes = lantern_fishes + new_lantern_fishes
        # print(f'After day {day + 1}\t', ','.join([str(f) for f in lantern_fishes]))
    
    print(f'Total fishes: {len(lantern_fishes)}')
        
    