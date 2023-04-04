from random import randint

HIDDEN_BOARD = [[" "] * 10 for x in range(10)]
GUESS_BOARD = [[" "] * 10 for y in range(10)]

letters_to_numbers = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
    'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
}


def print_board(board):
    print('  A B C D E F G H I J')
    print('  ___________________')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    for ship in range(10):
        ship_row, ship_column = randint(0, 9), randint(0, 9)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 9), randint(0, 9)
        board[ship_row][ship_column] = 'X'


def get_ship_location():
    row = input('Enter a ship row 1-10: ')
    while row not in '0123456789':
        print('Please enter a valid "Integer" for row')
        row = input('Enter a ship row 1-10: ')
    column = input('Enter a ship column A-J: ').upper()
    while column not in 'ABCDEFGHIJ':
        print('Please enter a valid "Character" for column')
        column = input('Enter a ship column A-J: ').upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1


create_ships(HIDDEN_BOARD)
print_board(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print('Welcome to BattleShipGalactica')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print('You have already guessed that')
    elif HIDDEN_BOARD[row][column] == 'X':
        print('Congratulations, You have hit the battleship')
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('You missed')
        GUESS_BOARD[row][column] = '-'
    if count_hit_ships(GUESS_BOARD) == 10:
        print('You won!!!')
        break
    print('You have' + str(turns) + 'turns remaining')
    if turns == 0:
        print('Game Over')
        break



