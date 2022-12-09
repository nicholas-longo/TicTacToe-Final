import random

computer_difficulty = "easy"
player_win_counter = 0 
computer_win_counter = 0 


class TicTacToe:
    #creates the tic-tac-toe board
    def __init__(self):
        self.board = []
        for r in range(3):
            row = ['-'] * 3
            self.board.append(row)
        
    #randomly decides if the player or the computer will start the game
    def get_starting_player(self) -> str:
        players = ("Player", "Computer")
        first_starting_player = random.choice(players)
        return first_starting_player

    #plays the computer's (O) turn
    def comp_turn(self) -> None:

        # easy mode. completely random gameplay
        is_valid_input = False
        while not is_valid_input:
            comp_row_position = random.randint(1, 3)
            comp_col_position = random.randint(1, 3)
            if self.board[comp_row_position - 1][comp_col_position - 1] != "-":
                continue
            self.board[comp_row_position - 1][comp_col_position - 1] = "O"
            is_valid_input = True
            print(f"The computer played row {comp_row_position} and column {comp_col_position} \n")

    #plays the player's (X) turn
    def player_turn(self) -> None:

        is_valid_input = False
        while not is_valid_input:

            # sanitizes the row input from user
            player_row_position = input("Enter the row number from integers 1-3: ")
            if not player_row_position.isdigit():
                print("Please select an integer from 1-3. \n")
                continue
            player_row_position = int(player_row_position)
            if not 1 <= player_row_position <= 3:
                print("Integer out of bounds. Please select an integer from 1-3. \n")
                continue

            # sanitizes the column input from user
            player_col_position = input("Enter the column number from integers 1-3: ")
            if not player_col_position.isdigit():
                print("Please select an integer from 1-3. \n")
                continue
            player_col_position = int(player_col_position)
            if not 1 <= int(player_col_position) <= 3:
                print("Integer out of bounds. Please select an integer from 1-3. \n")
                continue

            # checks to see if a position was already taken
            if self.board[player_row_position - 1][player_col_position - 1] != "-":
                print("That space is taken, please try another. \n")
                continue
            self.board[player_row_position - 1][player_col_position - 1] = "X"
            is_valid_input = True

    #displays the board including the updates spaces
    def show_board(self) -> None:
        for row in self.board:
            print(' '.join(row))
        print("\n")

    #checks if player or computer has won the game
    def check_win(self) -> bool:
        #check rows 
        global player_win_counter
        global computer_win_counter
        counter = 0
        for row in range(len(self.board)):
            position_value = self.board[row][0]
            counter = 0
            for col in range(3):
                if position_value == "-":
                    break
                if self.board[row][col] == position_value:
                    counter += 1 #the first iteration is guaranteed to make counter at least 1
                if counter == 3:
                    if position_value == "X":
                        player_win_counter += 1
                    if position_value == "O":
                        computer_win_counter += 1
                    print(f"{position_value} wins! \n")
                    self.show_board()
                    return True

        #check columns
        counter = 0
        for col in range(len(self.board)):
            position_value = self.board[0][col]
            counter = 0
            for row in range(3):
                if position_value == "-":
                    break
                if self.board[row][col] == position_value:
                    counter += 1
                if counter == 3:
                    if position_value == "X":
                        player_win_counter += 1
                    if position_value == "O":
                        computer_win_counter += 1
                    print(f"{position_value} wins!\n")
                    self.show_board()
                    return True

        #check diagonal (top left to right bottom)
        counter = 0
        position_value = self.board[0][0]
        for row in range(len(self.board)): 
            if position_value == "-":
                break
            if position_value == self.board[row][row]:
                counter += 1
            if counter == 3: 
                if position_value == "X":
                    player_win_counter += 1
                if position_value == "O":
                    computer_win_counter += 1
                print(f"{position_value} wins! \n")
                self.show_board()
                return True

        #check diagonal (top right to bottom left)
        counter = 0
        #bottom left value
        position_value = self.board[0][len(self.board)-1]
        for row in range(len(self.board)):
            if position_value == "-":
                break
            if position_value == self.board[row][len(self.board)-1 -row]:
                counter += 1
            if counter == 3: 
                if position_value == "X":
                    player_win_counter += 1
                if position_value == "O":
                    computer_win_counter += 1
                print(f"{position_value} wins!\n")
                self.show_board()
                return True

        return False
            
    #checks if there is a draw
    def check_draw(self) -> bool:
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    return False
        print("It's a draw! \n")
        self.show_board()
        return True

    #starts the game
    def game_on(self) -> None:
        self.set_difficulty()
        print("\n")
        starting_player = self.get_starting_player()
        print(starting_player, "will start the game!")
        if starting_player == "Player":
            while True:
                self.show_board()
                self.player_turn()
                if self.check_win() or self.check_draw():
                    break
                self.show_board()
                self.comp_turn()
                if self.check_win() or self.check_draw():
                    break

        else:
            while True:
                self.comp_turn()
                if self.check_win() or self.check_draw():
                    break
                self.show_board()
                self.player_turn()
                if self.check_win() or self.check_draw():
                    break
                self.show_board()
        
        self.play_again()
        
    #asks the user if they would like to play again
    def play_again(self) -> None:

        is_valid_input = False
        while not is_valid_input:
            play_again = input("Type Y to play again or N to quit: ")
            #checks if input is not a letter
            if not play_again.isalpha(): 
                print("Please type Y to play again or N to quit. \n")
                continue
            #checks if the character is a y or n
            if play_again.upper() != "Y" and play_again.upper() != "N":
                print("Please type Y to play again or N to quit. \n")
                continue
            if play_again.upper() == "Y":
                is_valid_input = True
                self.reset_board()
                self.game_on()
            if play_again.upper() == "N":
                print(f"You won {player_win_counter} times!")
                print(f"The computer won {computer_win_counter} times!")
                print("Thanks for playing!")
                is_valid_input = True
            
    #resets the board for a new game
    def reset_board(self) -> None:
        self.board = []
        for r in range(3):
            row = ['-'] * 3
            self.board.append(row)

    def set_difficulty(self) -> None:
        global computer_difficulty
        is_valid_input = False 
        while not is_valid_input: 
            computer_difficulty = input("Select difficulty 'easy', 'medium', or 'hard': ")
            if not computer_difficulty.isalpha():
                print("Please select a valid difficulty.")
                continue
            if not (computer_difficulty == "easy" or computer_difficulty == "medium" or computer_difficulty == "hard"):
                print("Please select a valid difficulty.")
                continue
            is_valid_input = True
            print(f"\nComputer Difficulty is set to {computer_difficulty}.")


def main():
    test = TicTacToe()
    test.game_on()


main()
