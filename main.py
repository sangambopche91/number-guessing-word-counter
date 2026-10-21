
import random
import string
from collections import Counter


# Game settings
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 7


# Play the number guessing game.
def play_game(best_score):
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0
    score = 0

    print("\n--- Number Guessing Game ---")
    print(f"Guess the number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print(f"You have {MAX_ATTEMPTS} attempts.")
    print("Each incorrect guess costs 10 points.")

    while attempts < MAX_ATTEMPTS:
        raw_guess = input("Enter your guess: ").strip()

        try:
            guess = int(raw_guess)
        except ValueError:
            print("Invalid input. Enter a whole number.")
            continue

        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print("Enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            score = max(0, 100 - 10 * (attempts - 1))
            print(f"Your score: {score}")

            if score > best_score:
                best_score = score
                print("New best score!")

            return best_score

        print(f"Attempts remaining: {MAX_ATTEMPTS - attempts}")

    print(f"Game over! The number was {secret_number}.")
    print("Your score: 0")
    return best_score


# Read a text file and count its words.
def count_words(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return

    # Remove punctuation and split the text into words.
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    counts = Counter(words)

    print("\n--- Word Counter Results ---")
    print("Total words:", len(words))
    print("Unique words:", len(counts))

    if not counts:
        print("The file is empty or contains no words.")
        return

    print("\nTop 10 most common words:")
    print(f"{'Word':<20}{'Count':>8}")
    print("-" * 28)

    for word, frequency in counts.most_common(10):
        print(f"{word:<20}{frequency:>8}")


# Display the application menu.
def main():
    best_score = 0

    while True:
        print("\n=== Python Mini Toolkit ===")
        print("1. Play Number Guessing Game")
        print("2. Count Words in a File")
        print("3. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            best_score = play_game(best_score)
            print(f"Best score this session: {best_score}")

        elif choice == "2":
            path = input(
                "Enter text file path (Enter for sample.txt): "
            ).strip()

            if not path:
                path = "sample.txt"

            count_words(path)

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Select 1, 2, or 3.")


if __name__ == "__main__":
    main()
