import typing


class BingoBoard:
    def __init__(self, values: typing.List[typing.List[int]]):
        self.values = values
        self.marked = [
            [None for column in row]
            for row in values
        ]
        self.winning_number = None

    def mark_number(self, number: int):
        if self.is_win():
            return

        for y in range(len(self.values)):
            for x in range(len(self.values[y])):
                if self.values[y][x] == number:
                    self.marked[y][x] = number

        if self.is_win():
            print(f"Self winning number: {number}")
            self.print()
            self.winning_number = number

    def print(self):
        for y in range(len(self.values)):
            print(
                '\t'.join(
                    [
                        f'({self.values[y][x]})'
                        if self.marked[y][x] is not None else
                        f'{self.values[y][x]}'
                        for x in range(len(self.values[y]))
                    ]
                )
            )

    def is_win(self) -> bool:
        for row in self.marked:
            if all([number is not None for number in row]):
                return True

        for column in zip(*self.marked):
            if all([number is not None for number in column]):
                return True
        return False

    def score(self) -> int:
        score_sum = 0
        
        for y in range(len(self.values)):
            for x in range(len(self.values[y])):
                if self.marked[y][x] is None:
                    score_sum += self.values[y][x]

        return score_sum * self.winning_number


class BingoBoardReader:
    @staticmethod
    def read(input_lines: typing.List[str]) -> typing.List[BingoBoard]:
        bingo_boards = []
        current_bingo_board_line = []

        for line in input_lines:
            if line == '':
                bingo_boards.append(
                    BingoBoard(
                        [
                            [
                                int(number)
                                for number in line.split(' ')
                                if number != ''
                            ]
                            for line in current_bingo_board_line
                        ]
                    )
                )
                current_bingo_board_line = []
                continue
            current_bingo_board_line.append(line)

        bingo_boards.append(
            BingoBoard(
                [
                    [
                        int(number)
                        for number in line.split(' ')
                        if number != ''
                    ]
                    for line in current_bingo_board_line
                ]
            )
        )
        return bingo_boards


if __name__ == '__main__':
    with open('input', 'r') as input_file:
        lines = input_file.read().split('\n')

        random_numbers = list(map(lambda x: int(x), lines[0].split(',')))
        bingo_boards = BingoBoardReader.read(lines[2:])
        last_winner = None

        for random_number in random_numbers:

            for bingo_board in bingo_boards:
                is_win_before_mark = bingo_board.is_win()
                bingo_board.mark_number(random_number)

                if is_win_before_mark == False and bingo_board.is_win():
                    last_winner = bingo_board

        print("\n\n\nLast Winner!")
        last_winner.print()
        print(f'Score: {last_winner.score()}')
        exit(0)
