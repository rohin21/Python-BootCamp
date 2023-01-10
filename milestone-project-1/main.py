from input import replay, player_input, player_choice
from board import place_marker, full_board_check
from win_check import win_check
from display import display
import random


def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


print("Welcome to Tic Tac Toe\n")

while True:

    game_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + "will go first\n")
    play_game = input("Ready to play game ? Enter y on n.\n")

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            display(game_board)
            position = player_choice(game_board)
            place_marker(game_board,player1_marker,position)

            if win_check(game_board,player1_marker):
                display(game_board)
                print("Player 1 has won. \n")
                game_on = False
            else:
                if full_board_check(game_board):
                    display(game_board)
                    print("This game is a tie. \n")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            display(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player2_marker, position)

            if win_check(game_board, player2_marker):
                display(game_board)
                print("Player 2 has won. \n")
                game_on = False
            else:
                if full_board_check(game_board):
                    display(game_board)
                    print("This game is a tie. \n")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay():
        break
