"""
Name: Kristina Rydbom
bumper.py

Problem: HW 8 bumper assignment.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
# from random import randint
import random


def main():
    # w, h, create window
    w = 700
    h = 500

    win = GraphWin("Bumper!", w, h)
    # win.setBackground(color_rgb(255, 255, 255))

    # radii and coordinates

    radius1 = 40
    radius2 = 40

    point_a = Point(300, 200)
    point_b = Point(500, 400)

    # creating circle 1!
    ball = Circle(point_a, radius1)
    ball.setFill("purple")
    ball.setOutline("purple")

    # creating circle 2!
    ball2 = Circle(point_b, radius2)
    ball2.setFill("green")
    ball2.setOutline("green")

    # draw!
    ball.draw(win)
    ball2.draw(win)

    # move_amount1 = randint(start1, end1)
    d1x = random.randint(0, 10)
    d1y = random.randint(-10, -1)
    d2x = random.randint(-10, -1)
    d2y = random.randint(0, 10)

    # for calculating distance
    c1x = point_a.getX()
    c1y = point_a.getY()
    c2x = point_b.getX()
    c2y = point_b.getY()
    formula = ((c1x - c2x) ** 2 + (c1y - c2y) ** 2) ** (1 / 2)
    distance = formula

    # while loop!
    while not win.checkMouse():
        # side to side
        if (ball.getCenter().getX() < 660) and (ball.getCenter().getX() > 40):
            ball.move(d1x, d1y)
            time.sleep(0.02)
        else:
            ball.move(-d1x, d1y)
            d1x = d1x * -1

        if (ball2.getCenter().getX() < 660) and (ball2.getCenter().getX() > 40):
            ball2.move(d2x, d2y)
            time.sleep(0.02)
        else:
            ball2.move(-d2x, d2y)
            d2x = d2x * -1

        # up and down
        if (ball.getCenter().getY() < 460) and (ball.getCenter().getY() > 40):
            ball.move(d1x, d1y)
            time.sleep(0.02)
        else:
            ball.move(d1x, -d1y)
            d1y = d1y * -1

        if (ball2.getCenter().getY() < 460) and (ball2.getCenter().getY() > 40):
            ball2.move(d2x, d2y)
            time.sleep(0.02)
        else:
            ball2.move(d2x, -d2y)
            d2y = d2y * -1

        # collision
        if (radius1 + radius2) == distance:
            ball.move(d1x, -d1y)
            d1y = d1y * -1
            ball2.move(-d2x, -d2y)

        # other methods
        # hit_vertical(), hit_horizontal(), get_random_color(), did_collide(Circle ball, Circle ball2)
        # confused about what to do with these methods... ?
        # if (ball.getCenter().getX() == 660) and (ball.getCenter().getX() == 40) and :
        #     return True
        # else:
        #     return False

    win.getMouse()

    win.close()


if __name__ == '__main__':

    main()
