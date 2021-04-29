import random

def game():
    player_input = input("Enter (r)ock, (p)aper, or (s)cissors.")

    while player_input not in "rps":
        player_input = input("Enter (r)ock, (p)aper, or (s)cissors.")

    options = ["r","p","s"]
    computer_choice = random.choice(options)

    if player_input == "r" and computer_choice == "s":
        print("You win!")
    elif player_input == "r" and computer_choice == "p":
        print("You lose!")
    elif player_input == "s" and computer_choice == "p":
        print("You win!")
    elif player_input == "s" and computer_choice == "r":
        print("You lose!")
    elif player_input == "p" and computer_choice == "r":
        print("You win!")
    elif player_input == "p" and computer_choice == "s":
        print("You lose!")
    else:
        print("Draw!")

    play_again = input("Play again? (y)es/(n)o")
    while play_again not in "yn":
        play_again = input("Play again? (y)es/(n)o")
    if play_again == "y":
        game()
    else:
        print("Goodbye.")


print("Ready to play?")
game()