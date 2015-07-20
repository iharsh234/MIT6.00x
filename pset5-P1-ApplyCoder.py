# PROBLEM 1: ENCRYPTION (APPLYCODER)

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    a1 = ''
    for x in text:
        if x in coder.keys():
          a1 = a1 + coder[x]
        else:
            a1 = a1 + x
    return a1
