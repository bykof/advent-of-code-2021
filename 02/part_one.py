class Submarine:
    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'

    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def forward(self, x):
        self.x += x

    def down(self, y):
        self.y += y
    
    def up(self, y):
        self.y -= y

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

print(f'Submarine Horizontal Position: {submarine.x} / Depth: {submarine.y}')
print(submarine.x * submarine.y)