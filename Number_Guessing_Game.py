import random


def guessing_game():
    while True:
        print("\nThis program outputs a random number between 1 and 10.")

        try:
            guess = int(input("Write your guess here: "))
            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
            continue

        rand = random.randint(1, 10)

        if guess == rand:
            print(f"🎉 You guessed right! It was {rand}.")
        else:
            print(f"❌ Wrong! The number was {rand}.")

        user_continue = input("Do you wish to continue? " "(yes/no): ").strip().lower()
        if user_continue == "no":
            print("Thanks for playing! Goodbye!")
            break
        elif user_continue != "yes":
            print("Invalid input. Please enter 'y' to continue or 'no' to exit.")


if __name__ == "__main__":
    guessing_game()
