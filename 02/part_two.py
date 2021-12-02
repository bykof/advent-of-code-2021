class Submarine:
    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'

    def __init__(self) -> None:
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def forward(self, x):
        self.horizontal += x
        self.depth += x * self.aim

    def down(self, y):
        self.aim += y
    
    def up(self, y):
        self.aim -= y

    def command(self, command: str, value: int):
        if command == Submarine.FORWARD:
            self.forward(value)
        if command == Submarine.DOWN:
            self.down(value)
        if command == Submarine.UP:
            self.up(value)


submarine = Submarine()

with open('input', 'r') as input_file:
    lines = input_file.readlines()
    
    for line in lines:
        command, value = line.split(' ')
        value = int(value)
        submarine.command(command=command, value=value)

print(f'Submarine Horizontal Position: {submarine.horizontal} / Depth: {submarine.depth}')
print(submarine.horizontal * submarine.depth)