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

    def is_horizontal_or_diagonal(self) -> bool:
        return (
            self.first_coordinate.x == self.second_coordinate.x or
            self.first_coordinate.y == self.second_coordinate.y
        )

    def __str__(self) -> str:
        return f'(x{self.first_coordinate.x}, y{self.first_coordinate.y}) - (x{self.second_coordinate.x}, y{self.second_coordinate.y})'


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
        from_y = line.first_coordinate.y
        to_y = line.second_coordinate.y
        from_x = line.first_coordinate.x
        to_x = line.second_coordinate.x
        current_y = from_y
        current_x = from_x
        self.values[current_y][current_x] += 1

        while not (current_x == to_x and current_y == to_y):
        
            if from_y < to_y:
                current_y += 1
            elif from_y > to_y:
                current_y -= 1

            if from_x < to_x:
                current_x += 1
            elif from_x > to_x:
                current_x -= 1

            self.values[current_y][current_x] += 1

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
                *list(map(lambda i: int(i), first_coordinates.split(',')))
            ),
            Coordinate(
                *list(map(lambda i: int(i), second_coordinates.split(',')))
            )
        )


with open('input', 'r') as input_file:
    input_lines = input_file.read().split('\n')

    lines = []
    max_x = 0
    max_y = 0

    for input_line in input_lines:
        line = LineReader.read(input_line)
        lines.append(line)
        print(line)
        
        if max_x < line.first_coordinate.x:
            max_x = line.first_coordinate.x
        if max_x < line.second_coordinate.x:
            max_x = line.second_coordinate.x
        if max_y < line.first_coordinate.y:
            max_y = line.first_coordinate.y
        if max_y < line.second_coordinate.y:
            max_y = line.second_coordinate.y
        
    max_x += 1
    max_y += 1

    print(f'Max X: {max_x}, Max Y: {max_y}')
    field = Field(max_x, max_y)
    for line in lines:
        field.draw_line(line)

    crosses = field.count_crosses()
    print(
        f"""
        Maximum Crosses Count: {crosses}"""
    )
