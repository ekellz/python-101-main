# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

num = random.randint(1, 10)
guess = None
attempt = 0

while guess != num:
    get_number = input("Please guess a number between 1 and 10: ")
    guess = int(get_number)
    attempt += 1

    if guess == num:
        print("Congrats, you win!")
        break
    elif attempt < 3: 
        print("Try again!")
    else:
        print("Sorry you exceeded your max attempts.")

