# Number Gussing Game 
import random

number = random.randint(1, 30)

while True:
    guess = int(input("Guess the number (1-30): "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number.")
        break
    