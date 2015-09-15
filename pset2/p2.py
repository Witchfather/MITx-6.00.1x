#PROBLEM 2: PAYING DEBT OFF IN A YEAR

#provided
#balance = 3926
#annualInterestRate = 0.2

#local
payment = 0
tempBalance = balance

while (True):
    payment += 10
    for i in range(1, 13):
        tempBalance = tempBalance - payment
        tempBalance = tempBalance + ((annualInterestRate/12) * tempBalance)
    if (tempBalance <= 0):
        break
    tempBalance = balance

print('Lowest Payment: ' + str(round(payment, 2)))
