def printAll(seq):
    if seq:
        print(seq, "->", seq[0])
        printAll(seq[1:])
""" With Tracing """
