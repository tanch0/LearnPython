import random

print(
    "Hello! Welcome to the number guessing game! I am thinking of a number between 1 and 100. Try to guess it! You have 10 tries."
)

randomNumber = random.randint(1, 100)
numberOfTries = 0
chance = 10

while numberOfTries < chance:
    guess = int(input("Enter your guess: "))
    numberOfTries += 1

    if guess == randomNumber:
        print(f"You guessed it! The correct answer was {randomNumber} in {numberOfTries} tries.")
        break

    elif guess < randomNumber:
        print("Your guess is too low.")

    elif guess > randomNumber:
        print("Your guess is too high.")

    if numberOfTries == chance:
        print("You have exceeded the number of tries. The correct answer was " + str(randomNumber))
