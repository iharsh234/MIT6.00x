# HAND LENGTH

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    harsh = hand.values()
    sum = 0
    for x in range(len(harsh)):
       sum = sum + harsh[x]
    return sum
    
