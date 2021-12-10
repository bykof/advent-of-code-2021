class ParseError(Exception):
    def __init__(self, expected_char: str, given_char: str, *args: object) -> None:
        self.expected_char = expected_char
        self.given_char = given_char
        super().__init__(*args)

    def __str__(self) -> str:
        return f'{self.expected_char} expected but found {self.given_char} instead'


class Stack:
    OPEN_CLOSE_MAP = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }

    def __init__(self) -> None:
        self._stack = []

    def parse(self, c: str):
        if len(self._stack) == 0:
            self._stack.append(c)
        else:
            if c in self.OPEN_CLOSE_MAP.keys():
                self._stack.append(c)
            elif c in self.OPEN_CLOSE_MAP.values():
                if self.OPEN_CLOSE_MAP[self._stack[-1]] == c:
                    del self._stack[-1]
                else:
                    raise ParseError(self.OPEN_CLOSE_MAP[self._stack[-1]], c)
            else:
                raise Exception(f'unknown char: {c}')


with open('input', 'r') as input_file:
    parse_errors = []
    lines = input_file.read().strip().splitlines()

    for line in lines:
        stack = Stack()
        print(line)

        for char in line:
            try:
                stack.parse(char)
            except ParseError as parse_error:
                parse_errors.append(parse_error)
                break
    
    points = 0
    count_map = {}
    points_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    
    for parse_error in parse_errors:
        if parse_error.given_char not in count_map:
            count_map[parse_error.given_char] = 0
        count_map[parse_error.given_char] += 1
    
    for char, counts in count_map.items():
        points += counts * points_map[char]
    print(points)
        