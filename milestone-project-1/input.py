# Take player input and validate.
from board import space_check


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1 choose X or O\n").upper()
    if marker == "X":
        return ("X","O")
    else:
        return ("0","X")


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Enter index position 1-9\n"))
    return position


def replay():
    choice = input("Play again ? Enter Yes or No.\n")
    return choice == 'Yes'