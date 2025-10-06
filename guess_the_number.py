import random

def guess():
    number = random.randint(1, 100)     
    total_attempts = 5               
    attempts = 0

    print("Welcome to Guess the Number!")
    print(f"You have {total_attempts} attempts to guess the number between 1 and 100.\n")

    while attempts < total_attempts:
        try:
            user_input = int(input("ENTER THE NUMBER (1-100): "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        attempts += 1

        if user_input == number:
            score = total_attempts - attempts + 1
            print(f"YOUR SCORE IS: {score}")
            print(f"YOUR GUESS IS CORRECT! You guessed it in {attempts} attempts.")
            break
        elif user_input > number:
            print("YOUR GUESS IS TOO HIGH\n")
        else:
            print("YOUR GUESS IS TOO LOW\n")

        # ✅ Show remaining attempts after each guess
        remaining_attempts = total_attempts - attempts
        print(f"You have {remaining_attempts} attempts left.\n")

    if user_input != number:
        print(f"YOU LOSE! The correct number was {number}.")

guess()
