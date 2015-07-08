__author__ = 'harsh'
#
# Hangman game
#

# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"  ## Download this txt file so that Hangman Could Guess a NUmber AT random

## https://courses.edx.org/asset-v1:MITx+6.00.1x_6+2T2015+type@asset+block/words.txt
## Make sure to have both HANGMAN and Words.txt in Same Directory.

def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    
    count = 0
    for x in range(len(secretWord)):
        if secretWord[x]  in lettersGuessed:
            count  = count+1
    if count == len(secretWord):
        return True
    else: return False



def getGuessedWord(secretWord, lettersGuessed):
    
    harsh = []
    for x in range(len(secretWord)):
        if secretWord[x]  in lettersGuessed:
            harsh.append(secretWord[x])
        else:
            harsh.append("_ ")
    return ''.join([harsh[x] for x in xrange(len(harsh))])



def getAvailableLetters(lettersGuessed):
    
    v = "abcdefghijklmnopqrstuvwxyz"
    h = []
    for x in v:
       if x in lettersGuessed:continue
       h.append(x)
    return ''.join([h[x] for x in xrange(len(h))])


def hangman(secretWord):
    
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is",len(secretWord),"letters long. "
    print  "-----------"
    n = 8
    print secretWord
    lettersGuessed = []
    while n>0:
        print "-----------"
        print "You have",n, "guesses left."
        print "Available letters:",getAvailableLetters(lettersGuessed)
        prompt="Please guess a letter: "
        guess = raw_input(prompt)
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed)
            continue
        lettersGuessed.append(guess)
        if isWordGuessed(secretWord, lettersGuessed) == True:
            return "Congratulations, you won!"

        if guess not in secretWord:
            n = n-1
            print "Oops! That letter is not in my word:",getGuessedWord(secretWord, lettersGuessed)
        else:
            n = n
            print "Good guess:",getGuessedWord(secretWord, lettersGuessed)
    if n==0:
        print "-----------"
        return "Sorry, you ran out of guesses. The word was",secretWord




secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

