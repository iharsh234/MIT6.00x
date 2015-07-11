# COMPUTER CHOOSES A WORD

def compChooseWord(hand, wordList, n):
       best = {}
       for word in wordList:
         if isValidWord(word,hand,wordList) == True:
            bestscore = getWordScore(word,n)
            best[word] = bestscore
       for name in best.keys():
          if best[name] == max(best.values()):
              return name
def compPlayHand(hand, wordList, n):
    sum = 0
    while calculateHandlen(hand) > 0:
      print "Current Hand: ", 
      displayHand(hand)
      word = compChooseWord(hand, wordList, n)
      if word == None:
           print "Total score:",sum,"points."
           return None
      points = getWordScore(word, n)
      sum = sum + points
      print "\"" +word + "\" earned",points, "points. Total:",sum,"points"
      print
      hand = updateHand(hand, word)
    print "Total score:",sum,"points."
    

