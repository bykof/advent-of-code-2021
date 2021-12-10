import typing


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
        self._is_fauly = False

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
                    self._is_fauly = True
                    raise ParseError(self.OPEN_CLOSE_MAP[self._stack[-1]], c)
            else:
                raise Exception(f'unknown char: {c}')

    def is_faulty(self):
        return self._is_fauly

    def incomplete(self) -> bool:
        return len(self._stack) > 0
    
    def chars_to_complete(self) -> typing.List[str]:
        chars_to_complete = []
        
        for stack_char in reversed(self._stack):
            chars_to_complete.append(self.OPEN_CLOSE_MAP[stack_char])
        return chars_to_complete

with open('input', 'r') as input_file:
    CHAR_SCORE_MAP = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    scores = []
    lines = input_file.read().strip().splitlines()

    for line in lines:
        stack = Stack()

        for char in line:
            try:
                stack.parse(char)
            except ParseError as parse_error:
                break
        
        if stack.incomplete() and not stack.is_faulty():
            score = 0
            chars_to_complete = stack.chars_to_complete()
            
            for char in chars_to_complete:
                score *= 5
                score += CHAR_SCORE_MAP[char]
            
            scores.append(score)
        
    
    scores = sorted(scores)
    print(scores[int(len(scores) / 2)])
        