# COMPUTER CHOOSES A WORD

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE (available within ps4b.py)
    best = {}
    for word in wordList:
        if isValidWord(word,hand,wordList) == True:
            bestscore = getWordScore(word,n)
            best[word] = bestscore
    for name in best.keys():
      if best[name] == max(best.values()):
         return name
