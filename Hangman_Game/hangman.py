import random

# List of predefined words
words = ["python", "apple", "ocean", "tiger", "planet"]

# Select a random word
secret_word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Display hidden word
display_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Game loop
while incorrect_guesses < max_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)

    # User input
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in secret_word:
        print("Correct guess!")

        # Update display word
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess

    # Wrong guess
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Final result
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game Over! The word was:", secret_word)
