# PAYING THE MINIMUM
def month(balance):
      new_balance = (( 1-monthlyPaymentRate)*balance) + ((( 1-monthlyPaymentRate)*balance) * annualInterestRate/12)
      return new_balance
print
n = 0
b = []
while n<12:
    print "Month:",n+1
    b.append(((balance*monthlyPaymentRate)))
    print "Minimum monthly payment:", ("{0:.2f}".format((balance*monthlyPaymentRate)))
    print "Remaining balance:", ("{0:.2f}".format(month(balance)))
    balance = month(balance)
    n = n+1
sum = 0.0
for x in xrange(len(b)):
    sum = sum +float(b[x])
print "Total paid:",("{0:.2f}".format(sum))
print "Remaining balance:",("{0:.2f}".format(balance))

# PAYING DEBT OFF IN A YEAR
def month(balance,x):
      new_balance = balance*(1+annualInterestRate/12) - x*(1+annualInterestRate/12)
      return new_balance
h = balance
n = 0
x = 10
d = []
for x in xrange(10,h,10):
    for a in range(12):
        balance = month(balance,x)
        if balance < 0.00:
            d.append(x)
    balance = h
print "Lowest Payment:",sorted(d)[0]

# USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER
def finalBalance(startBalance, annualInterestRate, monthlyPayment):
    for month in range(12):
        startBalance -= monthlyPayment
        startBalance *= (1 + (annualInterestRate / 12))
    return startBalance

accuracy = 0.000001
lower = balance / 12
upper = (balance * ((1 + (annualInterestRate/12)) ** 12)) / 12
payment = 0.5 * (upper + lower)
finalBal = finalBalance(balance, annualInterestRate, payment)
while abs(finalBal) > accuracy:
    if finalBal< 0:
        upper = payment
    else:
        lower = payment
    payment = 0.5 * (upper + lower)
    finalBal = finalBalance(balance, annualInterestRate, payment)
print("Lowest payment: {0:.2f}".format(payment))
