#PROBLEM 1: PAYING THE MINIMUM

#provided
#balance = 4213
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

#local
totalPaid = 0
for i in range(1, 13):
    minimumMontlyPayment = balance * monthlyPaymentRate
    totalPaid += minimumMontlyPayment
    balance = balance - minimumMontlyPayment
    balance = balance + ((annualInterestRate/12) * balance)
    print 'Month: ' + str(i)
    print 'Minimum monthly payment: ' + str(round(minimumMontlyPayment, 2))
    print 'Remaining balance: ' + str(round(balance, 2))

print('Total paid: ' + str(round(totalPaid, 2)))
print('Remaining balance: ' +  str(round(balance, 2)))
