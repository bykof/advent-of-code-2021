import typing


class BingoBoard:
    def __init__(self, values: typing.List[typing.List[int]]):
        self.values = values
        self.marked = [
            [False for column in row]
            for row in values
        ]

    def mark_number(self, number: int):
        for y in range(len(self.values)):
            for x in range(len(self.values[y])):
                if self.values[y][x] == number:
                    self.marked[y][x] = True

    def print(self):
        for y in range(len(self.values)):
            print(
                '\t'.join(
                    [
                        f'({self.values[y][x]})'
                        if self.marked[y][x] else
                        f'{self.values[y][x]}'
                        for x in range(len(self.values[y]))
                    ]
                )
            )
    
    def is_win(self) -> bool:
        for row in self.marked:
            if all(row):
                return True

        for column in zip(*self.marked):
            if all(column):
                return True
        return False
    
    def score(self, number: int) -> int:
        score_sum = 0
        
        for y in range(len(self.values)):
            for x in range(len(self.values[y])):
                if not self.marked[y][x]:
                    score_sum += self.values[y][x]
        
        return score_sum * number


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
        for random_number in random_numbers:
            print(f'Random Number: {random_number}')
            for bingo_board in bingo_boards:
                bingo_board.mark_number(random_number)
                if bingo_board.is_win():
                    print("BINGO")
                    print(f"Score: {bingo_board.score(random_number)}")
                    exit(0)
            
        
