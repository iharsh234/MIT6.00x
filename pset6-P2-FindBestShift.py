def findBestShift(wordList, text):
    text = "".join((char if char.isalpha() else " ") for char in text).split()
    max_valid = 0
    best_shift = 0

    for shift in range(26):
        num_valid = 0

        for word in text:
            plaintext = applyShift(word, shift)
            if isWord(wordList, plaintext):
                num_valid += 1

        if num_valid > max_valid:
            max_valid = num_valid
            best_shift = shift

    return best_shift
