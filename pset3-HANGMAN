# A WORDGAME: HANGMAN
# STEP-1
#  IS THE WORD GUESSED

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    count = 0
    for x in range(len(secretWord)):
        if secretWord[x]  in lettersGuessed:
            count  = count+1
    if count == len(secretWord):
        return True
    else: return False
    
# STEP-2
# PRINTING THE USER GUESS  

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    harsh = []
    for x in range(len(secretWord)):
        if secretWord[x]  in lettersGuessed:
            harsh.append(secretWord[x])
        else:
            harsh.append("_ ")
    return ''.join([harsh[x] for x in xrange(len(harsh))])
    
# STEP-3
# PRINTING ALL AVAILABLE LETTERS

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
  
    v = "abcdefghijklmnopqrstuvwxyz"
    h = []
    for x in v:
       if x in lettersGuessed:continue
       h.append(x)
    return ''.join([h[x] for x in xrange(len(h))])
    

# FINAL STEP
# HANGMAN THE GAME

def hangman(secretWord):
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is",len(secretWord),"letters long. "
    n = 8
    lettersGuessed = []
    while n>0:
        print "-----------"
        print "You have",n, "guesses left."
        print "Available Letters:",getAvailableLetters(lettersGuessed)
        prompt="Please guess a letter: "
        guess = raw_input(prompt)
        guess = guess.lower()
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed)
            continue
        lettersGuessed.append(guess)
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print "Good guess:",getGuessedWord(secretWord, lettersGuessed)
            print "-----------"
            print "Congratulations, you won!"
            break

        if guess not in secretWord:
            n = n-1
            print "Oops! That letter is not in my word:",getGuessedWord(secretWord, lettersGuessed)
        else:
            n = n
            print "Good guess:",getGuessedWord(secretWord, lettersGuessed)
    if n==0:
        print "-----------"
        print "Sorry, you ran out of guesses. The word was",secretWord


    
    
