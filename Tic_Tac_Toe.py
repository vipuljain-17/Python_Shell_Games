### Game called Tic Tac Toe

#Import lib
import random

#board numpad can be used to enter the position value
board = ["*"] * 9
left = list(range(9))

#Display board
def print_board():
    print()
    print(f" {board[6]}  |  {board[7]}  |  {board[8]}")
    print("----------------")
    print(f" {board[3]}  |  {board[4]}  |  {board[5]}")
    print("----------------")
    print(f" {board[0]}  |  {board[1]}  |  {board[2]}")
    print()


#Check for win
def check_win():

    #Total 8 possible ways to win
    all_wins = [(0,4,8), (2,4,6), (6,3,0), (7,4,1), (8,5,2), (6,7,8), (3,4,5), (0, 1, 2)]

    for win in all_wins:
        a,b,c = win
        if board[a] == board[b] == board[c]:
            if board[a] == "*":
                continue
            
            return True

    return False

#Check for Draw
def check_draw():
    if check_win():
        return False
    
    for i in range(9):
        if board[i] == "*":
            return False
    
    return True

#Check whether safe
def check_safe(i):
    return board[i] == "*"

def play(curr_player, player1_name, player2_name):
    print("Let's start the game. Enter 'quit' at any moment to quit the current game.")
    while True:
        while True:
            print_board()
            place = input(f"Enter a value(1-9) to place your mark {curr_player}: ")

            if place == "quit":
                if curr_player == "X":
                    print(f"Congratulations, {player2_name.upper()} you won!!!!")
                else:
                    print(f"Congratulations, {player1_name.upper()} you won!!!!")

                print()
                print("Thanks for playing. Until next time, See ya.")
                quit()
                
            elif place == "mark":
                random_choice = random.choice(left)
                print(f"The Comp has chosen to place mark at {random_choice+1}")
                board[random_choice] = curr_player
                left.remove(random_choice)

            else:
                try:
                    place = int(place)
                
                except ValueError:
                    print("Invalid input. Try Again")
                    continue
                
                if place < 1 or place > 9:
                    print("Invalid input. Try Again")
                    continue
                
                elif check_safe(place-1) == False:
                    print("Already Taken. Try another value.")
                    continue

                board[place-1] = curr_player
                left.remove(place-1)

            #Check for win
            if check_win():
                print_board()
                if curr_player == "X":
                    print(f"Congratulations, {player1_name.upper()} you won!!!!")
                else:
                    print(f"Congratulations, {player2_name.upper()} you won!!!!")
                print()
                return

            #Check for draw
            if check_draw():
                print_board()
                print("Match ended in draw!")
                return
            
            #Change placeholder after every turn
            if curr_player == "X":
                curr_player = "O"
            else:
                curr_player = "X"


if __name__ == "__main__":

    #Name Inputs
    print()
    player1_name = input("Enter the name of the player 1: ")
    player2_name = input("Enter the name of the player 2: ")
    print()

    #placehoolders
    player1 = "X"
    player2 = "O"

    print(f"{player1_name} has been assigned: {player1}")
    print(f"{player2_name} has been assigned: {player2}")

    
    play(player1, player1_name, player2_name)

    while True:
        print("1 to exit")
        print("2 to play again")

        try:
            end_input = int(input("Enter a value(1 or 2): "))
        except ValueError:
            print("Not an appropriate choice.Try Again")
            continue

        if end_input == 1:
            print()
            print("Thanks for playing. Until next time, See ya.")
            break

        elif end_input == 2:
            board = ["*"] * 9
            left = list(range(9))
            play(player1, player1_name, player2_name)