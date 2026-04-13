import random

def number_guess_game():
    print("Welcome to the Number Guessing Game")
    print("I have selected a number between 1 and 20.")
    number_guess_game = random.randint(1, 20)
    attempts = 0
    max_attempts = 7
    while attempts <  max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}: Enter your guess: "))
        
        except ValueError:
            print("Please Enter a Valid Interger.")
            continue
        
        attempts += 1

        if guess == number_guess_game:
            print(f"Congratulations! You've guessed the number {number_guess_game}in {attempts} attempts")
            break
        elif guess < number_guess_game:
            print("Too low! Try again.")
        else:
            print("too high! Try again.")
    else:
        print(f"Sorry, you have used all {max_attempts} attempts. The number was {number_guess_game}.")

# Ask if user wants to play again

    play_again = input("\n Do you want to play again? (yes/no): ").lower()
    if play_again in ['yes', 'y']:
        number_guess_game()
    else:
        print('Thank you for playing! Goodbye!')

if __name__ == "__main__":
    number_guess_game()