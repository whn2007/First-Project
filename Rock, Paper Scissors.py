import random

def game():

    while True:
        player_input = input("Enter (r)ock, (p)aper, or (s)cissors.")
        if player_input in "rps":
            break

    options = ["r","p","s"]
    computer_choice = random.choice(options)

    if player_input == "r" and computer_choice == "s":
        print("Computer chose scissors!")
        print("You win!")
    elif player_input == "r" and computer_choice == "p":
        print("Computer chose paper!")
        print("You lose!")
    elif player_input == "s" and computer_choice == "p":
        print("Computer chose paper!")
        print("You win!")
    elif player_input == "s" and computer_choice == "r":
        print("Computer chose rock!")
        print("You lose!")
    elif player_input == "p" and computer_choice == "r":
        print("Computer chose rock!")
        print("You win!")
    elif player_input == "p" and computer_choice == "s":
        print("Computer chose scissors!")
        print("You lose!")
    elif player_input == computer_choice:
        if computer_choice == "r":
            print("Computer chose rock!")
        elif computer_choice == "s":
            print("Computer chose scissors!")
        else:
            print("Computer chose paper!")
        print("Draw!")
    else:
        raise ("Not valid input.")

    while True:
        play_again = input("Play again? (y)es/(n)o")
        if play_again in "yn":
            break
    if play_again == "y":
        game()
    else:
        print("Goodbye.")


print("Ready to play?")
game()