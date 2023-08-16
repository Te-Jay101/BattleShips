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

    def print_grid(self, grid):
        print("   " + " ".join(map(str, range(self.grid_size))))
        print("  +" + "-" * (2 * self.grid_size - 1) + "+")
        for i, row in enumerate(grid):
            print(f"{i} |{' '.join(row)}|")
        print("  +" + "-" * (2 * self.grid_size - 1) + "+")