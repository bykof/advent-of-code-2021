import string

class SignalWire:
    def __init__(self, input_letter) -> None:
        self.input_letter = input_letter
        self.output_letter = input_letter

class SignalPatternMatcher:

    LENGTH_TO_PATTERN_MAP = {
        2: 'cf',
        4: 'bcdf',
        3: 'acf',
        7: 'abcdefg',
    }

    SIGNAL_PATTERN = {
        'cagedb': 0,
        'ab': 1,
        'gcdfa': 2,
        'fbcad': 3,
        'eafb': 4,
        'cdfbe': 5,
        'cdfgeb': 6,
        'dab': 7,
        'acedgfb': 8,
        'cefabd': 9
    }

    def __init__(self) -> None:
        self.signal_wires = []
        self.setup()

    def setup(self):
        for letter in string.ascii_lowercase[:7]:
            self.signal_wires.append(SignalWire(letter))
    
    def get_signal_wire(self, input_letter: str) -> SignalWire:
        for signal_wire in self.signal_wires:
            if signal_wire.input_letter == input_letter:
                return signal_wire
        raise Exception(f'could not find signalwire with input letter {input_letter}')

    def fit_signal_pattern(self, signal_pattern: str) -> int: 
        if len(signal_pattern) in self.LENGTH_TO_PATTERN_MAP.keys():
            for i in range(len(signal_pattern)):
                signal_wire = self.get_signal_wire(signal_pattern[i])
                signal_wire.output_letter = self.LENGTH_TO_PATTERN_MAP[len(signal_pattern)][i]
                print(f'mapping: {signal_wire.input_letter} -> {signal_wire.output_letter} for pattern {signal_pattern}')

    def read_digit(self, digit: str) -> int:
        for i in range(len(digit)):
            signal_wire = self.get_signal_wire(digit[i])
            print("before ", digit)
            digit = digit[:i] + signal_wire.output_letter + digit[i+1:]
            print("after ", digit)
        return self.SIGNAL_PATTERN[digit]
    
    def is_matching_easy_digit(self, digit: str) -> bool:
        print(digit, self.LENGTH_TO_PATTERN_MAP.keys(), len(digit) in list(self.LENGTH_TO_PATTERN_MAP.keys()))
        return len(digit) in list(self.LENGTH_TO_PATTERN_MAP.keys())
    
    def print_signal_wires(self):
        for signal_wire in self.signal_wires:
            print(f'{signal_wire.input_letter} -> {signal_wire.output_letter}')

        
        
with open('input', 'r') as input_file:
    lines = input_file.read().strip().split('\n')
    signal_pattern_matcher = SignalPatternMatcher()
    count = 0
    
    for line in lines:
        signal_patterns, digits = line.split(' | ')
        signal_patterns = signal_patterns.split(' ')
        digits = digits.split(' ')
        
        for digit in digits:
            if signal_pattern_matcher.is_matching_easy_digit(digit):
                count += 1
        
    print(count)