import random


class BattleshipsGame:
    """
    Main board class, sets the board for the game including size, ships.
    Has methods for showing the boards and adding ships.
    """
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
        self.player_shots = 25
        self.computer_shots = 25
        self.player_guesses = set()
        self.computer_guesses = set()

        self.add_player_ships_to_board()

    def create_random_ship(self):
        """
        Generates random coordinates for a ship on the game board.
        Returns a tuple (row, column).
        """
        return random.randint(0, 4), random.randint(0, 4)

    def draw_board(self, game_board):
        """
        Prints the given game board to the console.
        """
        for row in game_board:
            print(*row)

    def add_player_ships_to_board(self):
        """
        Adds player's ships to the player's game board.
        """
        self.player_game_board[self.player_ship1[0]][self.player_ship1[1]] = "S"
        self.player_game_board[self.player_ship2[0]][self.player_ship2[1]] = "S"
        self.player_game_board[self.player_ship3[0]][self.player_ship3[1]] = "S"
        self.player_game_board[self.player_ship4[0]][self.player_ship4[1]] = "S"

    def play_again(self):
        """
        Asks the player if they want to play again.
        """
        try_again = input("Play again? Yes or No? >: ").lower()
        if try_again == "yes":
            self.play_game()
        else:
            print("Sorry to see you go!")
            return

    def play_game(self):
        """
        Starts and manages the main game loop.
        """
        print("Welcome to BattleShips!"
              "\nYour challenge is to destroy all your enemies ships!\n")

        print("""\nTask:
        \nYou have 25 Shots and the enemy has 4 ships.
        \nIn order to hit them, you have to enter numbers for each location.
        \nLike so:
        \nFor the first row and first column, you have to write 1 and 1.
        \nGood luck on your conquest!\n""")

        while self.player_shots and self.computer_shots:
            print("\nYour board:")
            self.draw_board(self.player_game_board)
            print("\nComputer's board:")
            self.draw_board(self.computer_game_board)

            self.player_turn()
            if self.computer_ships_left == 0:
                print("Congratulations! You win!")
                self.play_again()
                break

            self.computer_turn()
            if self.player_ships_left == 0:
                print("Oh no! The computer sunk all of your ships. You lose!")
                self.play_again()
                break

    def player_turn(self):
        """
        Handles the player's turn by allowing them to make guesses on the computer's board.
        """
        try:
            row = int(input("Enter a row number between 1-5 >: "))
            column = int(input("Enter a column number between 1-5 >: "))
        except ValueError:
            print("Only enter numbers!")
            return self.player_turn()

        if row not in range(1, 6) or column not in range(1, 6):
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

    def computer_turn(self):
        """
        Handles the computer's turn by allowing it to make guesses on the player's board.
        """
        while True:
            guess = self.create_random_ship()
            if guess in self.computer_guesses:
                continue
            self.computer_guesses.add(guess)

            if guess == self.player_ship1 or guess == self.player_ship2 or guess == self.player_ship3 or guess == self.player_ship4:
                print("\nOh no! The computer hit your ship!\n")
                self.player_game_board[guess[0]][guess[1]] = "X"
                self.player_ships_left -= 1
                self.computer_shots -= 1
                break
            else:
                print("\nThe computer missed!\n")
                self.player_game_board[guess[0]][guess[1]] = "/"
                self.computer_shots -= 1
                break


if __name__ == "__main__":
    game = BattleshipsGame()
    game.play_game()
