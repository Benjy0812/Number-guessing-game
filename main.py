import random
import os


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


while True:

    print("This program outputs a random number between 1 and 10")
    print("Guess a number between 1 and 10")

    guess = int(input("Write you guess here: "))

    rand = random.randint(1, 10)

    if guess == rand:
        print(f"You guessed right it was {rand}")
    else:
        print(f"Wrong the number was {rand}")

    print("Do you wish to continue? Y/N")
    user_continue = input("Enter Here: ").upper()

    if user_continue == "N":
        clear_console()
        print("Good bye")
        break
