import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = int(input("Enter your number: "))
count = 0
while True:
    count += 1
    guess = random.randint(smaller,larger)
    if guess != myNumber:
        print("The computer is guessing " + str(guess))
    elif guess == myNumber:
        print("The computer guessed the number " + str(guess) + " in " ,count,"tries!")
        break
