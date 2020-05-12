def isSorted(myList):
    for i in range(len(myList)-1):
        if myList[i] >= myList[i+1]:
            return False
    return True

def main():
    myList = input("Enter a list of integers: >> ")
    myList = list(map(int, myList.split()))
    if (isSorted(myList)) :
        print ("The list is sorted in ascending order")
    else:
        print ("The list is not sorted in ascending order")

main()
