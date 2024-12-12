import time
import random
def print_hangman(stage):
    stages = [
        """
           ------
           |    |
                |
                |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        =========
        """
    ]
    print(stages[stage])
    time.sleep(0.5)

# Choose a random word from the word list
def get_word():
    word_list = ["python", "hangman", "programming", "developer", "technology"]
    return random.choice(word_list).upper()

# The main hangman game logic
def play_hangman():
    word = get_word()
    word_completion = "_"* len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6

    print("Welcome to Hangman!")
    print_hangman(0)
    print(word_completion)
    print("\n")

    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}.")
            elif guess != word:
                print(f"{guess} is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid guess.")

        print_hangman(6 - attempts)
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Sorry, you ran out of attempts. The word was {word}. Better luck next time!")

# Run the game
if __name__ == "__main__":
    play_hangman()
