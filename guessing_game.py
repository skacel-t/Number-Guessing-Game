import random

#game code
def start_game():
    player_guess = 'initialize'
    attempts = 0
    answer = random.randint(0,10)
    while player_guess != answer:
        try:
            player_guess = int(input(f"Guess a number between 0 and 10:  "))
            if player_guess > 10 or player_guess < 0:
                raise Exception("That number is out of range. Try again.")
        except ValueError as err: 
            print("Please enter a whole number.")
        except Exception as err:
            print(f"{err}")
        else:    
            attempts += 1
            if player_guess < answer:
                print("It's higher!")
            elif player_guess > answer:
                print("It's lower!")
    return attempts            

#Initializing variables
high_score = 'No high score yet.'
play_again = 'y' 

#Running the game
print("\n------------------------------------ \nWelcome to the Number Guessing Game! \n------------------------------------\n")
while play_again.lower() == 'y':
    print(f"------------------------------------\nHigh Score: {high_score}\n")
    attempts = start_game()
    if high_score == "No high score yet.":
        high_score = attempts
        play_again = input(f"\nCongratulations, you got it in {attempts} attempts! That is a new High Score! Would you like to play again? Y/N  ")
    elif high_score > attempts:
        high_score = attempts
        play_again = input(f"\nCongratulations, you got it in {attempts} attempts! That is a new High Score! Would you like to play again? Y/N  ")
    elif high_score == attempts:
        play_again = input(f"\nCongratulations, you got it in {attempts} attempts! You tied the High Score! Would you like to play again? Y/N  ")
    else:
        play_again = input(f"\nCongratulations, you got it in {attempts} attempts! Would you like to play again? Y/N  ")
        
print("\nThanks for playing, goodbye!")    