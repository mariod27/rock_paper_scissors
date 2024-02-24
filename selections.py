import random


def get_user_selection():
    """User is asked to enter a selection."""
    user_input = input("Enter a choice (rock, paper, scissors): ")
    selection = (user_input)
    return selection


def get_computer_selection():
    """Computer selects an option at random."""
    options = ['rock', 'paper', 'scissors']
    selection = random.choice(options)
    return selection


def determine_winner(user_pick, computer_pick):
    """The game is played.
    Conditional statements are used to determine the winner 
    between user_pick and computer_pick."""
    if user_pick == computer_pick:
        print(f"Both players selected {user_pick.title()}. It's a tie!")
    elif user_pick == 'rock':
        if computer_pick == 'scissors':
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_pick == 'paper':
        if computer_pick == 'rock':
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_pick == 'scissors':
        if computer_pick == 'paper':
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
