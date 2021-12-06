class Coordinate:
    def __init__(
        self,
        x: int,
        y: int,
    ) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(
        self,
        first_coordinate: Coordinate,
        second_coordinate: Coordinate,
    ) -> None:
        self.first_coordinate = first_coordinate
        self.second_coordinate = second_coordinate

    def is_allowed(self) -> bool:
        return (
            self.first_coordinate.x == self.second_coordinate.x or
            self.first_coordinate.y == self.second_coordinate.y
        )

    def __str__(self) -> str:
        return f'({self.first_coordinate.x}, {self.first_coordinate.y}) - ({self.second_coordinate.x}, {self.second_coordinate.y})'


class Field:
    def __init__(self, max_x=1, max_y=1) -> None:
        self.values = [
            [
                0
                for x in range(max_x)
            ]
            for y in range(max_y)
        ]

    def draw_line(self, line: Line):
        start_y = line.first_coordinate.y
        stop_y = line.second_coordinate.y

        if start_y > stop_y:
            temp = stop_y
            stop_y = start_y
            start_y = temp
        
        for y in range(start_y, stop_y+1):
            start_x = line.first_coordinate.x
            stop_x = line.second_coordinate.x

            if start_x > stop_x:
                temp = stop_x
                stop_x = start_x
                start_x = temp

            for x in range(start_x, stop_x+1):
                self.values[y][x] += 1

    def print(self):
        for y in self.values:
            print(
                ' '.join(
                    '.'
                    if x == 0 else str(x)
                    for x in y
                )
            )

    def count_crosses(self) -> int:
        count = 0

        for row in self.values:
            for x in row:
                if x >= 2:
                    count += 1

        return count


class LineReader:
    @staticmethod
    def read(line_string: str) -> Line:
        """
        '0,9 -> 5,9'
        """
        first_coordinates, second_coordinates = line_string.split(' -> ')
        return Line(
            Coordinate(
                *list(map(lambda x: int(x), first_coordinates.split(',')))
            ),
            Coordinate(
                *list(map(lambda y: int(y), second_coordinates.split(',')))
            )
        )


with open('input', 'r') as input_file:
    input_lines = input_file.read().split('\n')

    lines = []
    max_x = 0
    max_y = 0
    for input_line in input_lines:
        line = LineReader.read(input_line)
        if not line.is_allowed():
            continue
        lines.append(line)
        if max_x < line.first_coordinate.x:
            max_x = line.first_coordinate.x + 1
        if max_x < line.second_coordinate.x:
            max_x = line.second_coordinate.x + 1
        if max_y < line.first_coordinate.y:
            max_y = line.first_coordinate.y + 1
        if max_y < line.second_coordinate.y:
            max_y = line.second_coordinate.y + 1

    print(f'Max X: {max_x}, Max Y: {max_y}')
    print(list(map(lambda x: str(x), lines)))
    field = Field(max_x, max_y)
    for line in lines:
        field.draw_line(line)

    crosses = field.count_crosses()
    print(
        f"""
        Maximum Crosses Count: {crosses}"""
    )
