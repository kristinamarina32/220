"""
Name: Kristina Rydbom
button.py

Problem: HW 9 button class.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        valid_x = self.shape.getP1().getX() <= point.getX() <= self.shape.getP2().getX()
        valid_y = self.shape.getP1().getY() <= point.getY() <= self.shape.getP2().getY()
        if valid_x and valid_y:
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
