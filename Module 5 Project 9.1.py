count = 0
sum = 0.0
while True:
    data = input("Please enter a number or press enter to quit: ")
    if data == "":
        break
    count += 1
    total = float(data)
    sum += total
    avg = (sum/count)
print("The Sum of the numbers is: ", sum)
print("The Average of the numbers is: ", avg)
