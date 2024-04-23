import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    
    while True:
        print("************************************************")
        print("Are you getting bored ....Want to play a game ????")
        print("Welcome to the task 3 Rock-Paper-Scissors Game!")
        print("")
        print("Enter your choice (rock, paper, or scissors) or 'quit' to exit:")
        user_choice = input().lower()
        
        if user_choice == 'quit':
            print("\nThanks for playing!! I hope you enjoy the game of rock paper and scissor")
            print("Final Scores - You:", user_score, "Computer:", computer_score)
            break
        
        if user_choice not in choices:
            print("Invalid choice! Please enter either 'rock', 'paper', or 'scissors'. Other option except this is not available")
            continue
        
        computer_choice = random.choice(choices)
        
        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print("Current Scores - You:", user_score, "Computer:", computer_score)

play_game()
