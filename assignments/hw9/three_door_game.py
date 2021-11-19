"""
Name: Kristina Rydbom
three_door_game.py

Problem: HW 9 Three Door Game.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
import random
from button import Button


def main():
    w = 600
    h = 500

    win = GraphWin("Three Door Game", w, h)

    rec = Rectangle(Point(100, 330), Point(200, 370))

    rec2 = rec.clone()
    rec2.move(150, 0)
    rec3 = rec.clone()
    rec3.move(300, 0)

    door1 = Button(rec, "Door 1")
    door2 = Button(rec2, "Door 2")
    door3 = Button(rec3, "Door 3")
    doors = (door1, door2, door3)

    for door in doors:
        door.draw(win)

    random_door = random.choice(doors)

    i_have = Text(Point(300, 150), "I have a secret door")
    i_have.draw(win)

    choose = Text(Point(300, 450), "Click to choose my door")
    choose.draw(win)

    close = Text(Point(300, 450), "Click to close")

    pt = win.getMouse()

    for door in doors:
        if door.is_clicked(pt):
            if door == random_door:
                i_have.setText("You win!")
                door.color_button("green")
                choose.undraw()
                close.draw(win)
            if door != random_door:
                i_have.setText("You lost!")
                door.color_button("red")
                choose.setText(random_door.get_label() + " is my secret door")

    win.getMouse()
    win.close()


if __name__ == '__main__':

    main()
