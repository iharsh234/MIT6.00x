# PROBLEM 6

def sumDigits(N):
    if N <10:
        return N%10
    return N%10 + sumDigits(N//10)
