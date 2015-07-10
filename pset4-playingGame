# PLAYING A GAME

def playGame(wordList):
    n = HAND_SIZE
    prompt = "Enter n to deal a new hand, r to replay the last hand, or e to end game:"
    d = []
    while True:
      play = raw_input(prompt)
      d.append(play)
      if play == 'r':
         if  'n' not in d:
           print "You have not played a hand yet. Please play a new hand first!"
         else:
           playHand(hand, wordList, n)

      elif play == 'n':
           hand = dealHand(n)
           playHand(hand, wordList, n)
      elif play != 'e' and play != 'n'and play!= 'n':
           print "Invalid command."
      else:
           break
