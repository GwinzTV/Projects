import random

# Hangman Game

# Function to check if a letter is in the chosen word
def check_letter(letter, word, guessed_letters):
    if letter in guessed_letters:
        print("You already guessed that letter!")
        return guessed_letters
    elif letter in word:
        print("Correct!")
        guessed_letters.append(letter)
        return guessed_letters
    else:
        print("Incorrect!")
        guessed_letters.append(letter)
        return guessed_letters

# Function to display the current state of the word with underscores for unguessed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += f"{letter} "
        else:
            display += "_ "
    return display

# Function to display incorrect letters
def display_incorrect_letters(word, guessed_letters):
    display = ""
    for letter in guessed_letters:
        if letter not in word:
            display += f"{letter} "
    return display

# Function to randomly return a word from a list of words
def choose_word(words):
    return random.choice(words)
        

# Created a function called play_game(). This is where we will start our game

def play_game():
    # difficulty level in terms of words in the list
    words_medium = ["python", "programming", "computer", "science", "hangman", "game"]
    words_hard = ["dilate", "wednesday", "ingenious", "appraise", "superb"]
    words_easy = ["ate","cat", "car", "bike", "dog", "bag", "hair", "shoe", "store", "snore", "happy", "post"]
    
    # difficulty level selection
    level = input("Choose your level Easy[E], Medium[M], Hard[H]:").upper()
       
    if level == 'E':
        word = choose_word(words_easy)
    elif level == 'M':
        word = choose_word(words_medium)
    elif level == 'H':
        word = choose_word(words_hard)
    else:        # Exception handling Block which gives the user 3 attempt to input the specified information
        try:
            print("\nPlease enter either 'E' 'M' or 'H'")
            level = input("Choose your level Easy[E], Medium[M], Hard[H]:").upper()
            if level == 'E':
                word = choose_word(words_easy)
            elif level == 'M':
                word = choose_word(words_medium)
            elif level == 'H':
                word = choose_word(words_hard)
                
            try:
                print("\nLast Chance select either 'E' 'M' or 'H'")
                level = input("Choose your level Easy[E], Medium[M], Hard[H]:").upper()
                if level == 'E':
                    word = choose_word(words_easy)
                elif level == 'M':
                    word = choose_word(words_medium)
                elif level == 'H':
                    word = choose_word(words_hard)
            except:
                print(' ')
        finally:    # Game is terminated after 3 incorrect inputs
            print("\nUnable to follow instructions\n    ******************\n     GAME TERMINATED\n    ******************\n")
            quit()

    # Created an empty list for guessed letters.
    guessed_letters = []
    # Created a variable for number of guesses.
    guesses_remaining = 6
    
    while True:
        print("\nGuesses remaining:", guesses_remaining)
        current_output = display_word(word, guessed_letters)
        print(current_output)
        guess = input("Guess a letter: ").lower()
        guessed_letters = check_letter(guess, word, guessed_letters)
        incorrect_guesses = display_incorrect_letters(word, guessed_letters)
        if incorrect_guesses != "":
            print("\nIncorrect guesses so far: " + incorrect_guesses + "\n")

        # Decrement the guess_remaining if the guess is not in word
        if guess not in word:
            guesses_remaining -= 1
            
        # Check to see if the user has won
        if "_" not in display_word(word, guessed_letters):
            print("Congratulations, you win!\n")
            print(f"The word is: {word} !!\n")
            break
        
        # check to see if the user has lost
        if guesses_remaining == 0:
            print('Sorry, you lose. The word was "' + word + '"')
            break


# Start the game
play_game()
