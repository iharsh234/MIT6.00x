# PROBLEM 1: ENCRYPTION (BUILDCODER)  

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    har = {}
    import string
    sum = 0
    for x in string.lowercase:
        if ord(x) < (ord('z')- shift+1 ):
            har[x] = chr(ord(x) + shift)
        else:
            har[x] =  chr(ord('a') + sum)
            sum = sum +1
    sum1 = 0
    for x in string.uppercase:
        if ord(x) < (ord('Z')- shift+1 ):
            har[x] = chr(ord(x) + shift)
        else:
            har[x] =  chr(ord('A') + sum1)
            sum1 = sum1 +1
    return har
