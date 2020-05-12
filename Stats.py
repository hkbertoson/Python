def Mean(numbers):
    if len(numbers) == 0:
        return 0
    numberSum = 0
    for num in numbers:
        numberSum += num
    return numberSum/(float)(len(numbers))

def Median(numbers):
    if len(numbers) == 0:
        return 0
    numbers.sort()
    length = len(numbers)
    Median = numbers[length//2]
    if length % 2 == 0:
        Median += numbers[(length//2) - 1]
        Median = Median/2.0
    return Median

def Mode(numbers):
    if len(numbers) == 0:
        return 0
    
    return max(numbers, key = numbers.count)

def Main():
    numbers = [1, 2, 3, 3, 4, 5]
    if Mean(numbers) == 3:
        print("Mean is working.")
    
    if Median(numbers) == 3:
        print("median is working.")
    
    if Mode(numbers) == 3:
        print("Mode is working.")

Main()
