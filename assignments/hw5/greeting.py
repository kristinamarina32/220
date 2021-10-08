"""
Name: Kristina Rydbom
greeting.py

Problem: Write a program that displays a heart/Valentine's Day card.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def main():
    # window
    win = GraphWin("Valentine's Card", 700, 500)

    point_a = Point(300, 200)

    # components of the heart
    circle_a = Circle(point_a, 50)
    circle_a.setFill("red")
    circle_a.setOutline("red")
    circle_b = circle_a.clone()
    circle_b.move(90, 0)
    p1 = Point(255, 220)
    p2 = Point(350, 350)
    p3 = Point(435, 220)
    tri = Polygon(p1, p2, p3)
    tri.setFill("red")
    tri.setOutline("red")

    # text 1
    inst_pt = Point(350, 80)
    message = Text(inst_pt, "Happy Valentine’s Day!")

    # draw!
    circle_a.draw(win)
    circle_b.draw(win)
    tri.draw(win)
    message.draw(win)

    win.getMouse()

    # arrow through heart
    line = Line(Point(180, 170), Point(500, 280))
    line.setArrow("last")
    line.draw(win)

    # text 2
    close = Point(350, 490)
    msg2 = Text(close, "Click anywhere to close")
    msg2.draw(win)

    win.getMouse()

    win.close()


if __name__ == '__main__':
    main()