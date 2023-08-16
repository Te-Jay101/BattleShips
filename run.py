# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

class BattleshipsGame:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.player_grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.computer_grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.computer_fleet = [(random.randint(0, grid_size-1), random.randint(0, grid_size-1)) for _ in range(5)]

  # Print the grid with row and column indices.
    def print_grid(self, grid):
        print("   " + " ".join(map(str, range(self.grid_size))))
        print("  +" + "-" * (2 * self.grid_size - 1) + "+")
        for i, row in enumerate(grid):
            print(f"{i} |{' '.join(row)}|")
        print("  +" + "-" * (2 * self.grid_size - 1) + "+")

    # Get the player's guess for row and column and checks if the guess is within valid range.
    def play(self):
        print("Welcome to Battleships!")
        self.print_grid(self.player_grid)
        while True:
            try:
                row = int(input("Enter row (0 to {}): ".format(self.grid_size - 1)))
                col = int(input("Enter column (0 to {}): ".format(self.grid_size - 1)))
                if row < 0 or row >= self.grid_size or col < 0 or col >= self.grid_size:
                    print("Warning: Guess is off-grid. Try again.")
                    continue

                if (row, col) in self.computer_fleet:
                    print("Congratulations! You sank a battleship!")
                    self.player_grid[row][col] = 'X'
                else:
                    print("Missed!")
                    self.player_grid[row][col] = 'O'
                
                self.print_grid(self.player_grid)
                self.computer_turn()
                self.print_grid(self.player_grid)

                if all(self.player_grid[row][col] == 'X' for row, col in self.computer_fleet):
                    print("Congratulations! You destroyed all enemy battleships! You win!")
                    break

         # The computer randomly selects a row and column to attack.           
     def computer_turn(self):
        row, col = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
        if self.computer_grid[row][col] == ' ':
            if (row, col) in self.computer_fleet:
                print("The computer sank one of your battleships!")
                self.computer_grid[row][col] = 'X'
            else:
                print("The computer missed!")
                self.computer_grid[row][col] = 'O'
        else:
            self.computer_turn()

# Create a BattleshipsGame object and start playing.
if __name__ == "__main__":
    grid_size = int(input("Enter grid size: "))
    game = BattleshipsGame(grid_size)
    game.play()