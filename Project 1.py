import math
def newtonSquare(x):
    tolerance = 0.000001
    estimate = 1.0
    print ("press enter to stop the calculation...")
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if  difference <= tolerance:
           break
    print ("The program's estimate:" + format(estimate))
    print ("Python's estimate:     " + format(math.sqrt(x)))

def main():
    while True:
        x = input('Enter a positive number or press "Enter" to exit: ')
        if x == '':
            break
        else:
            newtonSquare(int(x))
main()
