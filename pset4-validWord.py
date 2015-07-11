# VALID WORDS

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    hand1 = hand.copy()
    for x in word:
        if x in hand1.keys():
            hand1[x] = hand1[x]-1
    word1 = getFrequencyDict(word)
    wordList1 = wordList
    if word not in wordList1:return False
    for x in word1:
        if x in hand1:
            if word1[x]>=hand1[x] and hand1[x] >=0:True
            else:
              return False
        else:
            return False
    return True
