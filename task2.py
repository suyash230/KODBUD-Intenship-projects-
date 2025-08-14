import random

secret_num = random.randint(1, 100)

print("Welcome to the Number Guessing Game ")
print("I have picked a number between 1 and 100. Can you guess it?")

tri = 0

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number...")
        continue

    guess = int(guess)
    tri += 1

    if guess == secret_num:
        print(f"Yay! You guessed it right in {tri} attempts.")
        break
    elif guess > secret_num:
        print("Too high! Try a smaller number.")
    else:
        print("Too low! Try a bigger number.")


