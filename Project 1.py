text = input("Enter text to encrypt: ")
d = int(input("Enter distance value: "))
etext = ""

for character in text:
    v = ord(character)
    c = v + d
    if c > ord('z'):
        c = ord('a') + d - (ord('z') - v + 1)
    etext = etext + chr(c)

print("Encrypted Text: " + etext)
