A = float(input("Please Enter Side 1: "))
B = float(input("Please Enter Side 2: "))
C = float(input("Please Enter Side 3: "))
if (A*A + B*B  == C*C)  or (B*B + C*C == A*A ) or (C*C + A*A == B*B):
    print("Right Triangle")
else:
    print("Not right")
