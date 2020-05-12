import math
def newton(x, estimate = 1.0):
    if abs(x-estimate ** 2) <= 0.000001:
        return estimate
    else:
        estimate = newton(x, (estimate + x / estimate) / 2)
    return estimate
def main():
    while True:
        x = input('Enter a positive number or press "Enter" to exit: ')
        if x == '':
            break
        else:
            print ("The program's estimate:" + format(newton(int(x))))
            print ("Python's estimate:     " + format(math.sqrt(int(x))))

main()
