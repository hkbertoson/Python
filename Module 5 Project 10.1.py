downPaymentRate = .10
monthlyPayRate = .05
annualInterestRate = .01

purchasePrice = float(input("Input purchase price: "))

downPayment = purchasePrice * downPaymentRate
baseCreditPrice = purchasePrice - downPayment
currentBalance = baseCreditPrice
monthlyPrincipal = baseCreditPrice * monthlyPayRate
monthlyInterest = currentBalance * annualInterestRate
monthlyPayment = monthlyPrincipal + monthlyInterest
principalVowed = monthlyPayment - monthlyInterest
month = 1

print('\n Item Price: $%.2f | Down Payment: $%.2f' % (purchasePrice, downPayment))
print('\n %5s %15s %17s %11s %9s %19s' % ('-----', '---------------------', '---------------', '----------------', '-------------', '-----------------'))
  
print(' %5s %15s %17s %11s %9s %19s' % ('Month', 'Current Total Balance', 'Interest Amount', 'Principal Amount', 'Month Payment', 'Balance Remaining'))
  
print('\n %5s %15s %17s %11s %9s %19s' % ('-----', '---------------------', '---------------', '----------------', '-------------', '-----------------'))

while currentBalance > 0.00:
       balanceRemaining = currentBalance - monthlyPayment
       if balanceRemaining < 0:
           balanceRemaining = 0
           monthlyPayment = currentBalance
       print(' %5s %15.2f %19.2f %16.2f %12.2f %19.2f' % (month, currentBalance, monthlyInterest, principalVowed, monthlyPayment, balanceRemaining))
       currentBalance = currentBalance - monthlyPayment
   
       monthlyInterest = balanceRemaining * annualInterestRate
 
       monthlyPayment = monthlyPrincipal + monthlyInterest
       if balanceRemaining < principalVowed:
           principalVowed = balanceRemaining - monthlyInterest
       else:
           principalVowed = monthlyPayment - monthlyInterest 
       month += 1
