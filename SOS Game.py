# FCAI - Programming 1 - 2022 - Assignment 1
# This program is a simple SOS game for 2 players
# Author: Abdullah Ibrahim   < abdullahibrahim1823@gmail.com >
# Version: 1.0
# Last modification date : 10/3/2022
# Copyright Ⓒ FCAI CU 2021-2022

game_board = [

    ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "1", "2", "3", "4", "empty"],
    ["empty", "5", "6", "7", "8", "empty"],
    ["empty", "9", "10", "11", "12", "empty"],
    ["empty", "13", "14", "15", "16", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]

]


# Display 4X4 game board
def display_game_board():
    print("")

    for row in range(1, 5):

        columns_counter = 0
        for column in range(1, 5):

            print(game_board[row][column], end='   ')
            columns_counter = columns_counter + 1

            if len(game_board[row][column]) == 1:  # to avoid inconsistency of lines
                print(" ", end='')
            if columns_counter == 4:
                print("\n")


# Get the letter that the player wants to play ( S or O )
def take_char():
    char = input("\nplease enter 'S' or 'O'...\n")
    while True:

        if char == 's' or char == 'S':  # to check the validation of the input
            take_location('S')  # pass the letter to this function to update the board
            break

        elif char == 'o' or char == 'O':  # to check the validation of the input
            take_location('O')  # pass the letter to this function to update the board
            break

        else:
            char = input("invalid input\n please enter 'S' or 'O'...\n")


# Get the location number where the player wants to put the letter
def take_location(char):
    location = input("please enter the location number...\n")
    isTrue = False

    while True:

        for row in range(5):
            for column in range(5):
                if game_board[row][column] == location and location != 'empty':  # to check the validation
                                                                                 # of the location number
                    game_board[row][column] = char  # updating the game board by replacing
                    isTrue = True  # the number with the letter

                    calculate_points(row, column, char)  # pass the 2D index of the new letter
                                                         # and pass the letter itself
        if isTrue:
            break
        else:
            location = input("invalid input\n please enter the location number...\n")


# Calculate points after every letter input by the players
def calculate_points(row_of_new_char, column_of_new_char, char):
    points = 0

    # To calculate the points if the input is ( S )
    if char == 'S':

        # check all character surrounding the character entered by the user
        for row in range(row_of_new_char - 1, row_of_new_char + 2):
            for column in range(column_of_new_char - 1, column_of_new_char + 2):

                if row == row_of_new_char and column == column_of_new_char:
                    continue

                if game_board[row][column] == 'O':  # to check if one of those characters is ( O )
                    new_row = row 
                    new_column = column

                    if new_row < row_of_new_char:  # check if the character (O) is in the row above (S)

                        if new_column < column_of_new_char:  # check if the character (O) is in the column left to (S)
                            if game_board[new_row - 1][new_column - 1] == 'S':
                                points += 1  # add 1 point if the word SOS formed in diagonal

                        if new_column == column_of_new_char:  # check if the character (O) is in the same column of (S)
                            if game_board[new_row - 1][new_column] == 'S':
                                points += 1  # add 1 point if the word SOS formed in Vertical

                        if new_column > column_of_new_char:  # check if the character (O) is in the column right to (S)
                            if game_board[new_row - 1][new_column + 1] == 'S':
                                points += 1  # add 1 point if the word SOS formed in diagonal

                    if new_row == row_of_new_char:  # check if the character (O) is in the same row of (S)

                        if new_column < column_of_new_char:
                            if game_board[new_row][new_column - 1] == 'S':
                                points += 1  # add 1 point if the word SOS formed in horizontal left to input

                        if new_column > column_of_new_char:
                            if game_board[new_row][new_column + 1] == 'S':
                                points += 1  # add 1 point if the word SOS formed in horizontal right to input

                    if new_row > row_of_new_char:  # check if the character (O) is in the row beneath (S)

                        if new_column < column_of_new_char:
                            if game_board[new_row + 1][new_column - 1] == 'S':
                                points += 1  # add 1 point if the word SOS formed in diagonal

                        if new_column == column_of_new_char:
                            if game_board[new_row + 1][new_column] == 'S':
                                points += 1  # add 1 point if the word SOS formed in vertical

                        if new_column > column_of_new_char:
                            if game_board[new_row + 1][new_column + 1] == 'S':
                                points += 1  # add 1 point if the word SOS formed in diagonal

    # To calculate the points if the input is ( O )
    elif char == 'O':
        row = row_of_new_char
        column = column_of_new_char

        if game_board[row][column - 1] == game_board[row][column + 1] == 'S':
            points += 1  # add 1 point if the word SOS formed in horizontal

        if game_board[row - 1][column] == game_board[row + 1][column] == 'S':
            points += 1  # add 1 point if the word SOS formed in vertical

        if game_board[row - 1][column - 1] == game_board[row + 1][column + 1] == 'S':
            points += 1  # add 1 point if the word SOS formed in diagonal

        if game_board[row + 1][column - 1] == game_board[row - 1][column + 1] == 'S':
            points += 1  # add 1 point if the word SOS formed in diagonal

    # pass calculated points scored by the player to this function to add these points to his total score
    add_points_to_player(points)


# To change the turn between the players
def change_turn():
    global current_player

    if current_player == player_1:
        current_player = player_2

    elif current_player == player_2:
        current_player = player_1


# To add calculated points to the total score of the current player
def add_points_to_player(new_points):
    global player_1_score
    global player_2_score

    if new_points == 0:
        change_turn()

    elif current_player == player_1:
        player_1_score += new_points

    elif current_player == player_2:
        player_2_score += new_points


# To display the score of each player
def display_score():
    print(player_1 + "'s score is " + str(player_1_score))
    print(player_2 + "'s score is " + str(player_2_score))


# To display which player has the turn
def display_current_turn():
    print("it is", current_player + "'s turn")


def is_winner():
    if player_1_score > player_2_score:
        print(player_1 + " is the winner!")
    elif player_2_score > player_1_score:
        print(player_2 + " is the winner!")
    else:
        print("DRAW!")


# To display GAME OVER and final game stats ( winner name or DRAW )
def game_over():
    print("\n \n")
    display_game_board()
    display_score()
    print("\n########## GAME OVER ##########\n")
    is_winner()


# This is the main function to play the game
def play_sos_game():
    counter = 0
    while True:
        display_game_board()
        display_score()
        display_current_turn()
        take_char()
        counter += 1

        if counter == 16:  # as the game board grid is 4x4 so if the counter reached 16 then the game is over
            game_over()
            return


# To take players names and declare score variables
player_1 = input("please enter player 1 name...\n")
player_2 = input("please enter player 2 name...\n")
current_player = player_1  # the first turn is for player 1

player_1_score = 0
player_2_score = 0

play_sos_game()  # To start playing the game
