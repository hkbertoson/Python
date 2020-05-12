text = input("Enter text to decrypt: ")
d = int(input("Enter distance value: "))
plainText = ""

for character in text:
    v = ord(character)
    c = v - d
    if c < ord('a'):
        c = ord('z') + (d + (ord('a') - v - 1))
    plainText = plainText + chr(c)

print("Decrypted Text: " + plainText)

