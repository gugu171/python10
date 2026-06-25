import random

while True:
    user_action = input("Enter a choice between rock, paper, and scissors: ")
    possible_action = ["rock","paper","scissors"]
    computer_action = random.choice(possible_action)
    print(f"\nYou chose {user_action}, the computer chose {computer_action}")

    if user_action == computer_action:
        print("Both of you selected",user_action,"it's a tie :D")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("OMG! You won because you chose rock, and the computer chose scissors! :D")
        else:
            print("rock smashes scissors :( . Better luck next time!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("O M GEE YOU WON! THIS IS BECAUSE YOU CHOSE PAPER, and the computer chose rock! :D")
        else:
            print("Uh oh :( . You lost because the computer chose paper and you chose rock :(")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors smashes paper! YOU WIN :D *epic music starts playing*")
        else:
            print("*sad music starts playing* NOOOOOOOOOOOO YOU LOST TO A COMPUTER BECAUSE YOU CHOSE PAPER AND IT CHOSE SCISSORS?! GEDDIM NEXT TIME >:(")

    play_again = input("Would YOU like to play again? (y/n) : ")
    if play_again == 'y':
        continue
    else:
        print("Ok! See you next time!")
        pass
