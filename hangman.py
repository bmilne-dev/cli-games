# a hangman program from scratch.

from random import randint

filename = "/home/pop/programming/python_files/word_list.txt"
with open(filename) as f:
    words = f.read()
word_list = words.split()

# define a function to select the word

def word_select(some_words):
    """choose a word for hangman from a word list"""
    
    some_word = some_words[randint(0, len(some_words) - 1)]
    return some_word

# define a function to display the word using an external 
# list of previous guesses

def display_word(some_word, my_guesses):
    """take the selected word and a list of user guesses
    and return a string that only shows previously guessed
    letters while replacing unknown letters with *"""

    hidden_list = []
    for letter in some_word:
        if letter in my_guesses:
            hidden_list.append(letter)
        else:
            hidden_list.append('*')
    return ''.join(hidden_list)

# define a function to receive the proper input
# meaning, the user can only input valid char's and only 1 at a time

def take_guess():
    """accept user guesses and make sure they are the 
    proper format"""

    user_guess = input("Take a guess!\n> ")
    while not user_guess.isalpha():
        user_guess = input("\nAlpha-Numeric characters only!"
                            "\nTake a guess!\n> ")
    while len(user_guess.strip()) > 1:
        user_guess = input("\nOne letter at a time please!"
                            "\nTake a guess!\n> ")
    return user_guess

# define a function to check if the guess is in the word

def check_guess(user_guess, some_word, my_guesses):
    """see if user guessed correctly!"""

    if user_guess in some_word:
        return True
    else:
        return False


word = word_select(word_list)
guesses = []
n = 0

print(f"Welcome to hangman!")

while True:
    if n == 6:
        print("Out of guesses!")
        print(f"The word was {word}!")
        break
    print(f"\nYou have {6 - n} guesses left")
    print("Your word:")
    print(display_word(word, guesses))
    guess = take_guess()
    guesses.append(guess)
    display = display_word(word, guesses)
    if display == word:
        print(f"You got it!")
        break
    elif not check_guess(guess, word, guesses):
        n += 1
   
