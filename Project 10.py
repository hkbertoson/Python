wage = int(input('Please Enter Hourly Wage: '))
hours = int(input('Please Enter Regular Hours Worked: '))
overtime = int(input('Please enter overtime hours worked: '))
pay = wage * hours
OtPay = overtime * wage * 1.5
total = pay + OtPay
print('Total weekly pay is: $' + str(total))


