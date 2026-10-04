import random
import string


# Number Guessing Game
def number_guessing_game():
    print("\n===== Number Guessing Game =====")

    secret_number = random.randint(1, 100)
    attempts = 0

    print("I have selected a number between 1 and 100.")
    print("Try to guess the number!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(f"Correct! The number was {secret_number}.")
                print(f"Total attempts: {attempts}")

                score = max(100 - (attempts - 1) * 10, 10)
                print(f"Your score: {score}")

                break

        except ValueError:
            print("Please enter a valid number.")


# Word Counter
def word_counter():
    print("\n===== Word Counter =====")

    filename = input("Enter the text file name: ")

    try:
        with open(filename, "r") as file:
            text = file.read()

        words = text.lower().split()

        word_frequency = {}

        for word in words:
            word = word.strip(string.punctuation)

            if word:
                word_frequency[word] = word_frequency.get(word, 0) + 1

        print("\n===== Word Frequency =====")

        for word, count in word_frequency.items():
            print(f"{word}: {count}")

        print(f"\nTotal words: {len(words)}")

    except FileNotFoundError:
        print("File not found. Please check the file name.")


# Main Menu
def main():
    while True:
        print("\n======================================")
        print(" Number Guessing Game & Word Counter")
        print("======================================")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()