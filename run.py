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

    def create_random_ship(self):
        return random.randint(0, 4), random.randint(0, 4)

    def draw_board(self, game_board):
        for row in game_board:
            print(*row)

     def add_player_ships_to_board(self):
        self.player_game_board[self.player_ship1[0]][self.player_ship1[1]] = "S"
        self.player_game_board[self.player_ship2[0]][self.player_ship2[1]] = "S"
        self.player_game_board[self.player_ship3[0]][self.player_ship3[1]] = "S"
        self.player_game_board[self.player_ship4[0]][self.player_ship4[1]] = "S"