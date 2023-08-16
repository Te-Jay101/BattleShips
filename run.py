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

def computer_guess(size, guessed_coordinates):
    while True:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        if (row, col) not in guessed_coordinates:
            return row, col

def main():
    print("Welcome to Battleships!".center(80))
    player_name = input("Enter your name: ")

    player_score, computer_score = 0, 0

    while input("Do you want to play? (yes/no): ").lower() == "yes":
        grid_size = 5  # 5 by 5 grid
        player_board = Board(grid_size, player_name)
        computer_board = Board(grid_size, "Computer")

        for _ in range(grid_size):
            player_board.place_ship()
            computer_board.place_ship()

        print(f"Let's begin, {player_name}!".center(80))
        player_won, computer_won = False, False
        player_guessed, computer_guessed = set(), set()

        while not player_won and not computer_won:
            player_board.print(computer_board)
            print("\n")

            player_row, player_col = get_user_guess(grid_size, player_guessed)
            player_guessed.add((player_row, player_col))
            player_won, computer_board = take_turn(player_row, player_col, computer_board, player_name)

            if not player_won:
                computer_row, computer_col = computer_guess(grid_size, computer_guessed)
                computer_guessed.add((computer_row, computer_col))
                computer_won, player_board = take_turn(computer_row, computer_col, player_board, "Computer")

        player_board.print(computer_board)
        if player_won:
            print(f"\nCongratulations, {player_name}! You've sunk all the computer's ships and won!".center(80))
            player_score += 1
        else:
            print("\nGame over! The computer has sunk all your ships.".center(80))
            computer_score += 1

        print(f"Scores - {player_name}: {player_score}, Computer: {computer_score}".center(80))

def take_turn(row, col, target_board, player):
    if target_board.grid[row][col] == 'S':
        print(f"{player} hit a ship!".center(80))
        target_board.grid[row][col] = '*'
        if all(cell != 'S' for row in target_board.grid for cell in row):
            return True, target_board
    else:
        print(f"{player} missed.".center(80))
        target_board.grid[row][col] = '/'
    return False, target_board
