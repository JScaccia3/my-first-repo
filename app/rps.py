import random
PLAYER_NAME="John"

# below reads the player name from notebook secrets listed as PLAYER_NAME
# or gives a default value


choices = ['rock', 'paper', 'scissors']

# variables for game stats
games_played = 0
games_won = 0

print(f"Welcome '{PLAYER_NAME}' to my Ultimate Rock-Paper-Scissors Game!")
print("Press Enter if you Wish to Continue")
input()
print("Let's Start! Your move!")

while True:
    # getting user input
    user_choice = input("Please choose a weapon ('rock', 'paper', 'scissors') or 'quit' to exit: ").lower()
    print("")

    # quit condition
    if user_choice == 'quit':
        if games_played > 0:
            win_percentage = (games_won / games_played) * 100
            print(f"Game Statistics for {PLAYER_NAME}:")
            print(f"Games Played: {games_played}")
            print(f"Games Won: {games_won}")
            print(f"Win Percentage: {win_percentage:.2f}%")
        else:
            print("No games played.")
        print(f"Thanks for playing, {PLAYER_NAME}! Goodbye!")
        break

    # if no valid option (Sana helped me with this part)
    if user_choice not in choices and user_choice != 'gun': #I added a cheat for fun
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors', or 'quit' to exit.")
        print("---")
        continue

    # display user choice
    print(f"{PLAYER_NAME}'s choice: '{user_choice}'")
    print("---")

    # generate random computer choice
    computer_choice = random.choice(choices)
    print(f"Computer's choice: '{computer_choice}'")
    print("---")

    # increment games
    games_played += 1

    # determine winner
    if user_choice == 'gun': #cheat code :)
        print(f"You used a gun! Pew Pew, {PLAYER_NAME} wins!")
        games_won += 1
    elif user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print(f"You won, {PLAYER_NAME}! Great job!")
        games_won += 1
    else:
        print("Computer wins, HAHA! Better luck next time!")

    print("---")

    # ask to play again?
    play_again = input("Would you like to play again? ('yes'/'no'): ").lower()
    if play_again != 'yes':

        if games_played > 0:
            win_percentage = (games_won / games_played) * 100
            print(f"Game Statistics for {PLAYER_NAME}:")
            print(f"Games Played: {games_played}")
            print(f"Games Won: {games_won}")
            print(f"Win Percentage: {win_percentage:.2f}%")
        else:
            print("No games played.")
        print(f"Thanks for playing, {PLAYER_NAME}! GOODBYE!")
        break
print("...IT'S OVER")
