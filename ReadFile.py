fileName = input("Enter a file name: ")
file = open(fileName, "r")
count = 0
for line in file:
    count = count + 1
print("The file has " + str(count) + " lines.");
file.close()
while True:
    try:
        n = int(input("Enter a line number [0 to quit]: "))
        lineno = 0
        break;
    except ValueError:
        print("Try again. Line number must be between 0 and " +str(count))
while n != 0:

        if n >= 0 and n <= count:
            file = open(fileName, "r")
            for line in file:
                lineno = lineno + 1
                if lineno == n:
                    print(line)
            file.close()
        else:
             print("Try again. Line number must be between 0 and " +str(count))
        while True:
            try:
                n = int(input("Enter a line number [0 to quit]: "))
                lineno = 0
                break;
            except ValueError:
                print("Try again. Line number must be between 0 and " +str(count))
