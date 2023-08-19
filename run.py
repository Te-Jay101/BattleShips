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
        self.computer_ship4 = self.create_random_ship()
        
        self.player_ship1 = self.create_random_ship()
        self.player_ship2 = self.create_random_ship()
        self.player_ship3 = self.create_random_ship()
        self.player_ship4 = self.create_random_ship()

        self.player_ships_left = 4
        self.computer_ships_left = 4
        self.player_shots = 10
        self.computer_shots = 10
        self.player_guesses = set()
        self.computer_guesses = set()
        
        self.add_player_ships_to_board()