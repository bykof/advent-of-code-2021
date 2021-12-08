import typing


class Configuration:
    def __init__(self) -> None:
        self.top = []
        self.top_left = []
        self.top_right = []
        self.center = []
        self.bottom = []
        self.bottom_left = []
        self.bottom_right = []

    # the signal pattern with 2 digits
    def add_one(self, signal_pattern: str):
        self.top_right = list(signal_pattern)
        self.bottom_right = list(signal_pattern)
        return signal_pattern

    # the signal pattern with 4 digits
    def add_four(self, signal_pattern: str):
        splitted_signal_pattern = list(signal_pattern)
        self.top_left = [
            digit for digit in splitted_signal_pattern if digit not in self.top_right]
        self.center = [
            digit for digit in splitted_signal_pattern if digit not in self.top_right]
        return signal_pattern

    # the signal pattern with 3 digits
    def add_seven(self, signal_pattern: str):
        splitted_signal_pattern = list(signal_pattern)
        self.top = [
            digit for digit in splitted_signal_pattern if digit not in self.top_right][0]
        return signal_pattern

    # two does not contain left top but center -> i know which letter is in center and top left
    def find_five(self, signal_patterns: typing.List[str]) -> str:
        for signal_pattern in signal_patterns:
            if len([digit for digit in self.top_left if digit in signal_pattern]) == 2:
                self.bottom_right = [
                    digit for digit in self.bottom_right if digit in signal_pattern][0]
                self.top_right = [
                    digit for digit in self.top_right if digit != self.bottom_right][0]
                return signal_pattern

    # contains the both right patterns
    def find_three(self, signal_patterns: typing.List[str]) -> str:
        for signal_pattern in signal_patterns:
            if self.bottom_right in signal_pattern and self.top_right in signal_pattern:
                self.center = [
                    digit for digit in self.center if digit in signal_pattern][0]
                self.top_left = [
                    digit for digit in self.top_left if digit != self.center][0]
                return signal_pattern

    def find_nine(self, signal_patterns: typing.List[str]) -> str:
        for signal_pattern in signal_patterns:
            if (
                self.top in signal_pattern and
                self.top_right in signal_pattern and
                self.top_left in signal_pattern and
                self.center in signal_pattern and
                self.bottom_right in signal_pattern
            ):
                self.bottom = [
                    digit
                    for digit in signal_pattern
                    if digit not in [
                        self.top,
                        self.top_right,
                        self.top_left,
                        self.center,
                        self.bottom_right
                    ]
                ][0]
                return signal_pattern

    def find_zero(self, signal_patterns: typing.List[str]) -> str:
        for signal_pattern in signal_patterns:
            if (
                self.center not in signal_pattern
            ):
                self.bottom_left = [
                    digit
                    for digit in signal_pattern
                    if digit not in [
                        self.top,
                        self.top_right,
                        self.top_left,
                        self.bottom_right,
                        self.bottom
                    ]
                ][0]
                return signal_pattern

    def match_number(self, digit_pattern: str) -> int:
        if (
            self.top_right in digit_pattern and
            self.bottom_right in digit_pattern and
            len(digit_pattern) == 2
        ):
            return 1

        if (
            self.top_right in digit_pattern and
            self.bottom_right in digit_pattern and
            self.top in digit_pattern and
            len(digit_pattern) == 3
        ):
            return 7

        if (
            self.top_right in digit_pattern and
            self.bottom_right in digit_pattern and
            self.top_left in digit_pattern and
            self.center in digit_pattern and
            len(digit_pattern) == 4
        ):
            return 4

        if (
            self.top in digit_pattern and
            self.top_left in digit_pattern and
            self.top_right in digit_pattern and
            self.bottom in digit_pattern and
            self.bottom_left in digit_pattern and
            self.bottom_right in digit_pattern and
            len(digit_pattern) == 6
        ):
            return 0

        if (
            self.top in digit_pattern and
            self.top_left in digit_pattern and
            self.top_right in digit_pattern and
            self.center in digit_pattern and
            self.bottom in digit_pattern and
            self.bottom_right in digit_pattern and
            len(digit_pattern) == 6
        ):
            return 9

        if (
            self.top in digit_pattern and
            self.top_left in digit_pattern and
            self.center in digit_pattern and
            self.bottom in digit_pattern and
            self.bottom_left in digit_pattern and
            self.bottom_right in digit_pattern and
            len(digit_pattern) == 6
        ):
            return 6

        if (
            self.top in digit_pattern and
            self.top_right in digit_pattern and
            self.center in digit_pattern and
            self.bottom in digit_pattern and
            self.bottom_left in digit_pattern and
            len(digit_pattern) == 5
        ):
            return 2
        
        if (
            self.top in digit_pattern and
            self.top_right in digit_pattern and
            self.center in digit_pattern and
            self.bottom_right in digit_pattern and
            self.bottom in digit_pattern and
            len(digit_pattern) == 5
        ):
            return 3

        if (
            self.top in digit_pattern and
            self.top_left in digit_pattern and
            self.center in digit_pattern and
            self.bottom_right in digit_pattern and
            self.bottom in digit_pattern and
            len(digit_pattern) == 5
        ):
            return 5
        
        if (
            self.top in digit_pattern and
            self.top_left in digit_pattern and
            self.top_right in digit_pattern and
            self.center in digit_pattern and
            self.bottom_left in digit_pattern and
            self.bottom_right in digit_pattern and
            self.bottom in digit_pattern and
            len(digit_pattern) == 7
        ):
            return 8

with open('input', 'r') as input_file:
    lines = input_file.read().strip().split('\n')
    all_numbers = 0

    for line in lines:
        configuration = Configuration()
        signal_patterns, digits = line.split(' | ')
        signal_patterns = signal_patterns.split(' ')
        digits = digits.split(' ')
        signal_pattern_two = None
        signal_pattern_four = None
        signal_pattern_three = None
        signal_pattern_five = []
        signal_pattern_six = []
        signal_pattern_seven = None

        for signal_pattern in signal_patterns:
            signal_pattern_length = len(signal_pattern)
            if signal_pattern_length == 2:
                signal_pattern_two = signal_pattern
            if signal_pattern_length == 3:
                signal_pattern_three = signal_pattern
            if signal_pattern_length == 4:
                signal_pattern_four = signal_pattern
            if signal_pattern_length == 5:
                signal_pattern_five.append(signal_pattern)
            if signal_pattern_length == 6:
                signal_pattern_six.append(signal_pattern)
            if signal_pattern_length == 7:
                signal_pattern_seven = signal_pattern

        configuration.add_one(signal_pattern_two)
        configuration.add_seven(signal_pattern_three)
        configuration.add_four(signal_pattern_four)
        configuration.find_five(signal_pattern_five)
        configuration.find_three(signal_pattern_five)
        configuration.find_nine(signal_pattern_six)
        configuration.find_zero(signal_pattern_six)

        number = 0
        places = [1000, 100, 10, 1]
        
        for i, digit in enumerate(digits):
            number += configuration.match_number(digit) * places[i]
        
        all_numbers += number
    print(all_numbers)