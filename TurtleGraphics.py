#TurtleGraphics.py
#Name: Blake Green 
#Date: 9/17/2025
#Assignment: turtle movements

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def drawPolygon(myTurtle, sides, size=100):
    angle = 360 / sides
    for i in range(sides):
        myTurtle.forward(size)
        myTurtle.right(angle)


def fillCorner(myTurtle, corner, size=100):
    drawSquare(myTurtle, size)
    myTurtle.penup()
    if corner == 1:
        myTurtle.goto(0,0)
    elif corner == 2:
        myTurtle.goto(50,0)
    elif corner == 3:
        myTurtle.goto(0,-50)
    elif corner == 4:
        myTurtle.goto(50, -50)
    #1-topleft,2-topright,3-bottomleft,4-bottomright
    myTurtle.pendown()
    myTurtle.begin_fill()
    drawSquare(myTurtle, size/2)
    myTurtle.end_fill()
    myTurtle.penup()
    

def squaresInSquares(myTurtle, num, size=50, step=20):
    for i in range(num):
        drawSquare(myTurtle, size + (i * 20))
        myTurtle.penup()
        myTurtle.backward(step / 2)
        myTurtle.left(90)
        myTurtle.forward(step / 2)
        myTurtle.right(90)
        myTurtle.pendown()

def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(5)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
