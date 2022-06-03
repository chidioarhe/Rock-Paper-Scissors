import random
import time


def print_pause(message_to_print):
    """Time function for code readability"""
    print(message_to_print)
    time.sleep(2)


print_pause("ROCK PAPER SCISSORS !!!")


def check_winner(player, computer):
    if computer == player:
        print_pause("It's a tie..")
        play_game()

    # computer victory scenarios.
    elif computer == "Rock" and player == "Scissors":
        print_pause("Rock crushes Scissors..")
        print_pause("CPU Wins.")
    elif computer == "Paper" and player == "Rock":
        print_pause("Paper covers Rock..")
        print_pause("CPU Wins.")
    elif computer == "Scissors" and player == "Paper":
        print_pause("Scissors cuts Paper..")
        print_pause("CPU wins.")
    # player victory scenarios
    elif computer == "Rock" and player == "Paper":
        print_pause("Paper covers Rock..")
        print_pause("Player wins!")
    elif computer == "Paper" and player == "Scissors":
        print_pause("Scissors cuts Paper..")
        print_pause("Player wins!")
    elif computer == "Scissors" and player == "Rock":
        print_pause("Rock crushes Scissors..")
        print_pause("Player wins!")


def play_game():
    new_input = ""
    while True:
        print_pause("Please select from options below:")
        print_pause("'R' for 'rock'")
        print_pause("'P' for 'paper'")
        print_pause("'S' for 'scissors'")
        new_input = input("Please enter an option from the above: ")
        is_valid = True
        if new_input == "P":
            player = "Paper"
        elif new_input == "R":
            player = "Rock"
        elif new_input == "S":
            player = "Scissors"
            # the choice is set to scissors by default
            pass
        else:
            print_pause("Invalid choice.")
            is_valid = False
        # only do the game logic if the choice was valid
        if is_valid:
            computer = random.choice(["Rock", "Paper", "Scissors"])
            print_pause(f"Player ({player}) : CPU ({computer})")
            check_winner(player, computer)
            break
            print_pause("\n")


play_game()
