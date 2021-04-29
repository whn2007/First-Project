import random

def game():
    player_input = input("Enter (r)ock, (p)aper, or (s)cissors.")

    while player_input not in "rps":
        player_input = input("Enter (r)ock, (p)aper, or (s)cissors.")

    options = ["r","p","s"]
    computer_choice = random.choice(options)

    if player_input == "r" and computer_choice == "s":
        print("You win!")
        input("Play again? (y)es/(n)o")

print("Ready to play?")
game()