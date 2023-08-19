import random

class BattleshipsGame:
    def __init__(self):
        self.player_game_board = [["O", "O", "O", "O", "O"],
                                  ["O", "O", "O", "O", "O"],
                                  ["O", "O", "O", "O", "O"],
                                  ["O", "O", "O", "O", "O"],
                                  ["O", "O", "O", "O", "O"]]
        
        self.computer_game_board = [["O", "O", "O", "O", "O"],
                                    ["O", "O", "O", "O", "O"],
                                    ["O", "O", "O", "O", "O"],
                                    ["O", "O", "O", "O", "O"],
                                    ["O", "O", "O", "O", "O"]]

        self.computer_ship1 = self.create_random_ship()
        self.computer_ship2 = self.create_random_ship()
        self.computer_ship3 = self.create_random_ship()
        