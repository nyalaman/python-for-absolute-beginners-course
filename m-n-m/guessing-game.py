print("-------------------------------")
print("    Smarties Guessing Game    ")
print("-------------------------------")

import random
mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

print("Guess the number of Smarties in the jar and you get lunch on the house!")
print()

while attempts < attempt_limit:
    guess_text = input("How many Smarties do you think are in the jar? ")
    guess = int(guess_text)
    attempts += 1

    if mm_count == guess:
        print("Congratulations! You guessed it right! Your lunch is on the house!")
        break
        print(f"Bye, you're done in {attempts}!")

    elif guess < mm_count:
        print("Too LOW! Try again.")
    else:
        print("Too HIGH! Try again.")0


