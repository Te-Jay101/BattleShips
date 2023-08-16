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

def get_user_guess(size, guessed_coordinates):
    while True:
        guess = input(f"Enter your guess (row column): ")
        try:
            row, col = map(int, guess.split())
            if (0 <= row < size and 0 <= col < size) and (row, col) not in guessed_coordinates:
                return row, col
            else:
                print("Guess is off-grid or has been used before. Try again.")
        except ValueError:
            print("Invalid input. Try again.")