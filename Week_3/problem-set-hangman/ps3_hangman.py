# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/joshuastevenson/Desktop/Machine-Learning/MITx_6.00.1x/Week_3/problem-set-hangman/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return len(list(filter(lambda x: x in lettersGuessed, secretWord))) == len(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    res = [l if l in lettersGuessed else '_' for l in secretWord]
    return ' '.join(res)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    return ''.join([l for l in letters if l not in lettersGuessed])


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    gameOn = True
    guesses = 8
    lettersGuessed = ''

    while gameOn:
        if guesses == 0:
            break
        print("-------------")
        print('You have {} guesses left.'.format(guesses))
        print("Available letters: {}".format(
            getAvailableLetters(lettersGuessed)))
        x = input("Please guess a letter: ")

        if x in lettersGuessed:
            print("Oops! You've already guessed that letter: {}".format(
                getGuessedWord(secretWord, lettersGuessed)))
            lettersGuessed += x
        elif x in secretWord:
            lettersGuessed += x
            print("Good guess: {}".format(
                getGuessedWord(secretWord, lettersGuessed)))
        else:
            lettersGuessed += x
            print("Oops! That letter is not in my word: {}".format(
                getGuessedWord(secretWord, lettersGuessed)))
            guesses -= 1

        if isWordGuessed(secretWord, lettersGuessed):
            gameOn = False
            return print("Congratulations, you won!")
    return print("Sorry, you ran out of guesses. The word was {}. ".format(secretWord))

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
