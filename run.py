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

    def play_again(self):
        try_again = input("Play again? Yes or No? >: ").lower()
        if try_again == "yes":
            self.__init__()
            self.play_game()
        else:
            print("Sorry to see you go!")
            return

    def play_game(self):
        print("Welcome to BattleShips!"
              "\nYour challenge is to find and destroy all your enemies ships!\n")

        print("""\nTask:
        \nYou have 10 Shots and the enemy has 3 ships.
        In order to hit them, you have to enter numbers for each location. like so:
        For the first row and first column, you have to write 1 and 1.
        Good luck on your conquest!\n""")

        while self.player_shots and self.computer_shots:
            print("\nYour board:")
            self.draw_board(self.player_game_board)
            print("\nComputer's board:")
            self.draw_board(self.computer_game_board)

            self.player_turn()
            if self.computer_ships_left == 0:
                print("Congratulations! You sunk all of the computer's ships. You win!")
                self.play_again()
                break

            self.computer_turn()
            if self.player_ships_left == 0:
                print("Oh no! The computer sunk all of your ships. You lose!")
                self.play_again()
                break

    def player_turn(self):
        try:
            row = int(input("Enter a row number between 1-5 >: "))
            column = int(input("Enter a column number between 1-5 >: "))
        except ValueError:
            print("Only enter numbers!")
            return self.player_turn()

        if row not in range(1, 6) or column not in range(1, 5):
            print("\nThe numbers must be between 1-5!")
            return self.player_turn()

        row -= 1  
        column -= 1  

        guess = (row, column)

        if guess in self.player_guesses:
            print("\nYou have already made that guess! Try again.\n")
            return self.player_turn()

        if self.computer_game_board[row][column] == "/" or self.computer_game_board[row][column] == "X":
            print("\nYou have already shot there! Try again.\n")
            return self.player_turn()
        elif guess == self.computer_ship1 or guess == self.computer_ship2 or guess == self.computer_ship3:
            print("\nBoom! You hit a ship!\n")
            self.computer_game_board[row][column] = "X"
            self.computer_ships_left -= 1
            self.player_guesses.add(guess)
        else:
            print("\nYou missed!\n")
            self.computer_game_board[row][column] = "/"
            self.player_shots -= 1
            self.player_guesses.add(guess)