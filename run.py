import random


class Board:
    def __init__(self, size, owner):
        self.size = size
        self.grid = [['O' for _ in range(size)] for _ in range(size)]
        self.owner = owner

    def place_ship(self):
        while True:
            row, col = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if self.grid[row][col] == 'O':
                self.grid[row][col] = 'S'
                break

    def print(self, other_board):
        print(f"{self.owner}'s Board:".ljust(40) + f"{other_board.owner}'s Board:")
        for i in range(self.size):
            player_row = ' '.join(self.grid[i])
            computer_row = ' '.join(
                [cell if cell in ['*', '/'] else 'O' for cell in other_board.grid[i]])
            print(f"{player_row.ljust(40)}{computer_row}")