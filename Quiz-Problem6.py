# PROBLEM 6
#Write a recursive Python function, given a non-negative integer N, to calculate and return the sum of its digits.

def sumDigits(N):
    if N <10:
        return N%10
    return N%10 + sumDigits(N//10)
