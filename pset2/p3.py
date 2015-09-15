#PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER

#provided
#balance = 999999
#annualInterestRate = 0.18

#local
monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
payment = 0.0
tempBalance = balance

while (True):
    payment = round(upperBound - ((upperBound - lowerBound) / 2.0), 3)
    for i in range(1, 13):
        tempBalance = tempBalance - payment
        tempBalance = tempBalance + ((annualInterestRate / 12.0) * tempBalance)
    if round(tempBalance, 2) == 0.0:
        break
    elif tempBalance < 0:
        upperBound = payment
    else:
        lowerBound = payment
    tempBalance = balance

print('Lowest Payment: ' + str(round(payment, 2)))
