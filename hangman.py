import random

# List of words for the game
word_list = ["programming", "hangman", "computer", "game", "processor", "register", "abstraction", "algorithm", "array", "application", "bandwidth", "binary", "bit", "boolean", "byte", "boot", "character", "client", "coding", "compiler", "casting", "concatenation", "database", "data", "debugging", "debug", "digital", "disk", "domain", "encryption", "executable", "execution", "exception", "file", "filename", "float", "for", "gigabyte", "identifier", "integer", "interface", "internet", "interpreter", "iteration", "kernel", "library", "list", "loader", "logic", "machine", "matrix", "memory", "modem", "node", "parameter", "peripheral", "procedure", "python", "radix", "record", "robotics", "router", "runtime", "selection", "sequence", "set", "software", "stack", "storage", "string", "subroutine", "syntax", "system", "upload", "user", "variable", "web"]

# Function to select a random word from the list
def select_random_word(word_list):
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Main Hangman game function
def hangman_game():
    word_to_guess = select_random_word(word_list)
    guessed_letters = []
    lives = 6

    print("Welcome to Hangman!")
    
    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print("\nWord:", current_display)
        print("Lives left:", lives)
        print("Guessed letters:", guessed_letters)

        if "_" not in current_display:
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        if lives == 0:
            print("Out of lives! The word was:", word_to_guess)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Wrong guess. You lose a life!")
            lives -= 1

    # Update and display the score
    score = lives
    print("\nYour score:", score)

    # Record the results in an external file
    with open("hangman_scores.txt", "a") as file:
        file.write(f"Word: {word_to_guess}, Score: {score}\n")

if __name__ == "__main__":
    while True:
        hangman_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break