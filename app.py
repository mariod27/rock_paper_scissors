from selections import *


while True:
    user_pick = get_user_selection()
    computer_pick = get_computer_selection()
    determine_winner(user_pick, computer_pick)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
