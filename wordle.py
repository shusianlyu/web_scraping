# ----------------------------------------------------------------------
# Name:      wordle
# Purpose:   implement the wordle game
# Author(s): Shu Sian (Jessie) Lyu, An Tran
# Date: 02/13/2023
# ----------------------------------------------------------------------
"""
Simple implementation of the wordle game

Player inputs a text file for wordle game to pick a 5-letter word.
The game prompts the user for 5 letter guesses.
Bad inputs are ignored and the player is prompted again.
Correctly placed letters are green.
Yellow letters are in the word, but misplaced.
Red letters are not in the word.
Feedback is given if the user guesses the right word or
the word is just given if the user doesn't guess in 6 tries.
"""
import string
import random

# Constant assignments
RED = '\033[91m'     # to print text in red: print(RED + text)
GREEN = '\033[92m'   # to print a letter in green: print(GREEN + text)
YELLOW = '\033[93m'  # to print a letter in yellow: print(YELLOW + text)
DEFAULT = '\033[0m'  # to reset the color print(DEFAULT + text)


def choose_wordle(filename):
    """
    Read the file specified and choose a random 5-letter word.
    :param filename: (string) name of the file to choose the wordle from
    :return: (string) the mystery word in uppercase
    """
    with open(filename, "r") as f:
        text = f.read()
        # remove leading and trailing punctuations
        # and skip words that contain non letters
        words = [word.strip(string.punctuation) for word in text.split()
                 if len(word.strip(string.punctuation)) == 5 and
                 word.strip(string.punctuation).isalpha()]

    return random.choice(words).upper()


def check(wordle, guess):
    """
    Check the player's guess against the wordle and return a string
    representing the color coded feedback for the specified guess.
    Red indicates that the guessed letter is NOT in the word.
    Yellow indicates that the letter is in the word but not in the
    correct spot.
    Green indicates that the letter is in the word in the correct spot.
    :param wordle: (string) the mystery word in upper case
    :param guess: (string) the user's guess in upper case
    :return: (string) a string of red, yellow or green uppercase letters
    """
    # enter your code below and take out the pass statement
    # HINTS: create a working list of letters in the wordle
    # go over the letters in the guess and check for green matches
    # add the green matches to their correct position in an output list
    # remove the green matches from the working list
    # go over the letters in the guess again
    # compare them to the letters in working list
    # add yellow or red color and add them to their position in output
    # list
    # join the output list into a colored string
    working_list = list(wordle)
    user_input = list(guess)
    result = user_input[:]

    # handle green matches
    for i in range(len(user_input)):
        if user_input[i] == working_list[i]:
            result[i] = GREEN + result[i]
            working_list[i] = ''

    # handle yellow and red matches
    for i in range(len(user_input)):
        if user_input[i] in working_list:
            # handle yellow matches
            working_list[i] = ''
            result[i] = YELLOW + result[i]
        else:
            # handle red matches
            result[i] = RED + result[i]

    return ''.join(result)


def feedback(attempt):
    """
    Print the feedback corresponding to the number of attempts
    it took to guess the wordle.
    :param attempt: (integer) number of attempts needed to guess
    :return: None
    """
    match attempt:
        case 1: print("Genius!")
        case 2: print("Magnificent!")
        case 3: print("Impressive!")
        case 4: print("Splendid!")
        case 5: print("Great!")
        case 6: print("Phew!")

    return None


def prompt_guess():
    """
    Prompt the user repeatedly for a valid 5 letter guess that contains
    only letters.  Guess may be in lower or upper case.
    :return: (string) the user's valid guess in upper case
    """
    while True:
        guess = input('Please enter your 5 letter guess: ')
        # validate guess
        if len(guess) == 5 and guess.isalpha():
            # break the loop if the guess is valid
            break

    return guess.upper()


def play(wordle):
    """
    Implement the wordle game with all 6 attempts.
    :param wordle: (string) word to be guessed in upper case
    :return: (boolean) True if player guesses within 6 attempts
             False otherwise
    """
    # enter your code below and take out the pass statement
    # call the prompt_guess function to prompt the user for each attempt
    # call the check function to build the colored feedback string
    # call the feedback function to print the final feedback if the user
    # guesses within 6 attempts
    attempt = 1  # attempt starts from 1
    while attempt <= 6:
        print(DEFAULT + f'Attempt {attempt}')
        guess = prompt_guess()  # prompt the user for guess
        result = check(wordle, guess)  # get the colored feedback
        print(result)
        # check if the user guesses within 6 attempts
        if guess == wordle:
            feedback(attempt)
            return True
        attempt += 1  # increment attempt by 1
    return False


def main():
    # enter your code following the outline below and take out the
    # pass statement.
    # 1. prompt the player for a filename
    # 2. call choose_wordle and get a random mystery word in uppercase
    #    from the file specified
    # 3. call play to give the user 6 tries
    # 4. if the user has not guessed the wordle, print the correct
    #    answer
    filename = input('Please enter the filename: ')
    wordle = choose_wordle(filename)  # get a random mystery word
    # check if the user has not guessed the wordle
    if not play(wordle):
        print(DEFAULT + f'The correct answer is {wordle}')


if __name__ == '__main__':
    main()
