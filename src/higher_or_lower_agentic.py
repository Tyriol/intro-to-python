from math import isqrt
from random import randint


PRIMES = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
)


def show_hint(number):
    parity = "even" if number % 2 == 0 else "odd"
    prime = "prime" if number in PRIMES else "not prime"
    square = "a square number" if isqrt(number) ** 2 == number else "not a square number"
    print(f"Hint: The number is {parity}, {prime}, and {square}.")


def play_game():
    number = randint(0, 100)
    guesses = 0

    print("Welcome to Higher or Lower! Guess an integer from 0 to 100.")
    print("Enter -1 to quit or -2 for a hint.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter an integer.")
            continue

        if guess == -1:
            print(f"You quit. The number was {number}. You made {guesses} guesses.")
            break
        if guess == -2:
            show_hint(number)
            continue
        if not 0 <= guess <= 100:
            print("Please enter a number from 0 to 100.")
            continue

        guesses += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You guessed {number} in {guesses} guesses.")
            break


if __name__ == "__main__":
    play_game()