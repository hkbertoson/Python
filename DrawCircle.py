from turtle import Turtle
import math

def drawCircle(t,x,y,radius):
    move = 2.0 * math.pi * radius/120
    count = 0
    t.up()
    t.goto(x,y)
    t.right(90)
    t.down()
    for count in range(120):
        t.right(3)
        t.forward(move)
        count += 1
    return

