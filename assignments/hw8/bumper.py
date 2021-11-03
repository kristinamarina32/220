"""
Name: Kristina Rydbom
bumper.py

Problem: HW 8  ---------

Certification of Authenticity:
I certify that this assignment is entirely my own work.
# """
from graphics import *
# from random import randint


def main():
    # window
    w = 700
    h = 500

    win = GraphWin("Bumper!", w, h)

    x1 = 300
    y1 = 200
    x2 = 500
    y2 = 400

    point_a = Point(x1, y1)
    point_b = Point(x2, y2)

    ball = Circle(point_a, 40)
    ball.setFill("purple")
    ball.setOutline("purple")

    ball2 = Circle(point_b, 40)
    ball2.setFill("green")
    ball2.setOutline("green")

    # draw!
    ball.draw(win)
    ball2.draw(win)

    for i in range(500):
        ball.move(-10, 0)
        ball2.move(10, 0)
        time.sleep(0.1)
        # if y1 == 500 or y1 == 0:
        #     ball.move(10, 0)
        if (x1 == 700) or (x1 == 0):
            ball.move(10, 0)


    win.getMouse()
#
    win.getMouse()

    win.close()


if __name__ == '__main__':

    main()
