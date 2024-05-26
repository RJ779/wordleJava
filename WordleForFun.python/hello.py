import random

# List of words for the game
words = ["apple", "scoop", "dates", "crate", "early"]


word = random.choice(words)


max_attempts = 5

for attempt in range(1, max_attempts + 1):
    # Get the user's guess
    guess = input(f"Attempt {attempt}/{max_attempts}. Guess a {len(word)}-letter word: ")

    # Check if the guess is valid
    if len(guess) != len(word):
        print("Invalid guess. Please enter a word with the correct length.")
        continue

    # Check if the guess is correct
    if guess == word:
        print("Congratulations! You guessed the word correctly!")
        break

    # Provide feedback on the guess
    feedback = ""
    for i in range(len(word)):
        if guess[i] == word[i]:
            feedback += "x"
        elif guess[i] in word:
            feedback += "o"
        else:
            feedback += "_"
    print(feedback)

    # Check if it was the last attempt
    if attempt == max_attempts:
        print(f"Game over! The word was '{word}'.")
