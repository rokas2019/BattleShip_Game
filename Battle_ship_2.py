import random

LETTERS_TO_NUMBERS = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
    'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
}


class Board:
    def __init__(self, size=10):
        self.size = size
        self.grid = [[' '] * size for _ in range(size)]

    def __str__(self):
        header = '    ' + ' '.join(chr(i) for i in range(ord('A'), ord('A') + self.size))
        rows = [f"{i + 1:2}|{'|'.join(self.grid[i])}|" for i in range(self.size)]
        return f"{header}\n {'  ' + '_' * (self.size * 2 + 1)}\n " + '\n '.join(rows)


class Game:
    def __init__(self, num_turns=10):
        self.hidden_board = Board()
        self.guess_board = Board()
        self.num_turns = num_turns

    def create_ships(self):
        for _ in range(10):
            row, col = random.randint(0, 9), random.randint(0, 9)
            while self.hidden_board.grid[row][col] == 'X':
                row, col = random.randint(0, 9), random.randint(0, 9)
            self.hidden_board.grid[row][col] = 'X'

    def get_ship_location(self):
        while True:
            try:
                row = int(input('Enter a ship row 1-10: ')) - 1
                col = LETTERS_TO_NUMBERS[input('Enter a ship column A-J: ').upper()]
                return row, col
            except (ValueError, KeyError):
                print('Please enter a valid row (1-10) and column (A-J)')

    def play(self):
        self.create_ships()
        while self.num_turns > 0:
            print('Welcome to BattleShip Galactica')
            print(self.guess_board)
            row, col = self.get_ship_location()
            if self.guess_board.grid[row][col] != ' ':
                print('You have already guessed that')
            elif self.hidden_board.grid[row][col] == 'X':
                print('Congratulations, You have hit the battleship')
                self.guess_board.grid[row][col] = 'X'
                self.num_turns -= 1
            else:
                print('You missed')
                self.guess_board.grid[row][col] = '-'
            if sum(row.count('X') for row in self.guess_board.grid) == 10:
                print('You won!!!')
                break
            print(f"You have {self.num_turns} turns remaining")
            self.num_turns -= 1
        else:
            print('Game Over')


game = Game()
game.play()


