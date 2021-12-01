"""
Name: Kristina Rydbom
lab4.py

Problem: Completed lab 4 problems (fixed for extra credit).

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can create a circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw an additional square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(150, 150), Point(50, 50))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the square
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of square

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() #- c.getX()
        dy = p.getY() #- c.getY()

        shape = Rectangle(Point(dx-10, dy-10), Point(dx+10, dy+10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
    inst_pt = Point(width / 2, height - 20)
    instructions.undraw()
    message = Text(inst_pt, "Click again to quit")
    message.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Draw a rectangle", 700, 500)
    message = Text(Point(350, 450), "Click on two points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    rec = Rectangle(p1, p2)
    rec.setFill("blue")
    rec.setOutline("purple")
    rec.draw(win)

    dx = p1.getX() - p2.getX()
    dy = p1.getY() - p2.getY()

    length = abs(dx)
    width = abs(dy)

    print(dx)
    print(dy)

    area = length * width
    print(area)
    msg = "Area = " + str(area)
    message1 = Text(Point(350, 400), msg)
    message1.draw(win)

    perimeter = (length * 2) + (width * 2)
    msg2 = "Perimeter = " + str(perimeter)
    message2 = Text(Point(350, 350), msg2)
    message2.draw(win)
    message.undraw()
    message_close = Text(Point(350, 450), "Click to end program")
    message_close.draw(win)

    win.getMouse()
    win.close()


def circle():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    instructions = Text(Point(200, 350), "Click to create circle")
    instructions.draw(win)
    center = win.getMouse()
    outer = win.getMouse()
    x1 = center.getX()
    x2 = outer.getX()
    y1 = center.getY()
    y2 = outer.getY()
    d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    msg_r = "Radius = " + str(round(d, 2))
    radius = Text(Point(200, 300), msg_r)
    radius.draw(win)
    print(d)
    shape = Circle(center, d)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    instructions.undraw()
    instructions2 = Text(Point(200, 350), "Click to close")
    instructions2.draw(win)
    win.getMouse()
    win.close()


def pi2():
    n = eval(input("Enter the number of terms in the series:"))
    product = 0
    switch = -1
    for i in range(n):
        switch = switch * -1
        num = 4
        den = 2*i + 1
        product = product + (num/den) * switch
    print("Product = ", product)


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
