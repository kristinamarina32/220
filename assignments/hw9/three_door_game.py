"""
Name: Kristina Rydbom
three_door_game.py

Problem: HW 9 game.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
import random
# from button import Button


def main():
    w = 600
    h = 500

    win = GraphWin("Three Door Game", w, h)

    rec = Rectangle(Point(100, 330), Point(200, 370))
    rec.setOutline("black")
    rec.draw(win)
    rec2 = rec.clone()
    rec2.move(150, 0)
    rec3 = rec.clone()
    rec3.move(300, 0)
    rec2.draw(win)
    rec3.draw(win)
    doors = (rec, rec2, rec3)

    random_door = random.choice(doors)

    i_have = Text(Point(300, 150), "I have a secret door")
    i_have.draw(win)

    choose = Text(Point(300, 450), "Click to choose my door")
    choose.draw(win)

    msg1 = Text(Point(150, 350), "Door 1")
    msg1.draw(win)

    msg2 = Text(Point(300, 350), "Door 2")
    msg2.draw(win)
    msg3 = Text(Point(450, 350), "Door 3")
    msg3.draw(win)

    win.getMouse()

    # rec2.setFill("green")

    # you_win = Text(Point(300, 150), "You win!")
    # #
    # if user.click() <= rec:
    #     rec.setFill("green")
    #     you_win.draw(win)

    i_have.undraw()
    choose.undraw()

    you_win = Text(Point(300, 150), "You win!")
    you_win.draw(win)

    close = Text(Point(300, 450), "Click to close")
    close.draw(win)
    #==============

    if random_door == doors[0] or random_door == doors[1] or random_door == doors[2]:
        random_door.setFill("green")
    else:
        random_door.setFill("red")

    win.getMouse()
    win.close()

    return random_door


if __name__ == '__main__':

    main()