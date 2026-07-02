import random

# List of predefined words
words = ["python", "apple", "school", "computer", "garden"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
incorrect_guesses = 0
max_incorrect = 6

# Display word with underscores
display_word = ["_"] * len(word)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_incorrect and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# Game result
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)