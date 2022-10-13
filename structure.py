import random

number = random.randint(1, 100)


# Function to choose the difficulty of the game.
def choose_difficulty():
    """
    :return: If the user types 'easy' they will have 10 attempts to guess the number, otherwise, if they type 'hard'
    they will have 5 attempts instead.
    """
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number.")
    return attempts


# Input that will allow the user to make a guess.
def user_guess():
    """
    :return: The user will choose a number between 1 and 100.
    """
    guess_number = int(input('Make a guess: '))
    return guess_number


# Check the number the user chose.
def check_guess():
    """
    :return: It will compare the user guess with the random number selected and depending on how many attempts remain,
    it will allow the user to try to guess the number once again, until they run out of attempts, and it will provide
    a hint if the number to guess is higher or lower than the number chose by the user.
    """
    num_attempts = choose_difficulty()
    user_number = user_guess()
    while num_attempts > 0:
        if user_number == number:
            print(f"You got it! The answer was {number}.")
            num_attempts = 0
        elif user_number > number:
            num_attempts -= 1
            print(f"Too high.")
        elif user_number < number:
            num_attempts -= 1
            print(f"Too low.")

        if num_attempts == 0:
            if user_number != number:
                print("You've run out of guesses, you lose.")
        else:
            print(f"Guess again.\nYou have {num_attempts} attempts remaining to guess the number.")
            user_number = user_guess()

