import random

name = input("Enter your name: ")
print(f"Hello {name}! Welcome to the word guessing game!")
print("I am thinking of a word. You have 10 tries to guess it.")

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
randomWord = random.choice(words)

guesses = ""
chance = 10
isWin = False

while chance > 0:
    failed = 0
    for char in randomWord:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        isWin = True
        break

    print()
    guess = input("Guess a letter: ")
    guesses += guess

    if guess not in randomWord:
        chance -= 1
        print(f"Wrong guess! You have {chance} chances left.")
        print(failed)

if isWin:
    print("Congratulations! You guessed the word.")
else:
    print("Sorry, you ran out of chances. The correct word was " + randomWord)