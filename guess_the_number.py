import random

def guess():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_input = int(input("ENTER THE NUMBER (1-100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if user_input == number:
            print(f"YOUR GUESS IS CORRECT! You guessed it in {attempts} attempts.")
            break
        elif user_input > number:
            print("YOUR GUESS IS TOO HIGH")
        else:
            print("YOUR GUESS IS TOO LOW")

guess()
