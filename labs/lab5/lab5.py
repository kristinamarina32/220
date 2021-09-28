import math
"""
Name: Kristina Rydbom
lab5.py

Problem: Complete lab 5 problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)
    message = Text(Point(350, 450), "Click on three points")
    message.draw(win)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    tri = Polygon(p1, p2, p3)
    tri.setFill("purple")
    tri.setOutline("black")
    tri.draw(win)

    # length calculations

    # side a length
    dx1 = p2.getX() - p1.getX()
    dy1 = p2.getY() - p1.getY()
    a = math.sqrt((dx1**2) + (dy1**2))

    # side b length
    dx2 = p3.getX() - p2.getX()
    dy2 = p3.getY() - p2.getY()
    b = math.sqrt((dx2 ** 2) + (dy2 ** 2))

    # side c length
    dx3 = p1.getX() - p3.getX()
    dy3 = p1.getY() - p3.getY()
    c = math.sqrt((dx3 ** 2) + (dy3 ** 2))

    # perimeter

    perimeter = a + b + c
    msg2 = "Perimeter = " + str(round(perimeter, 2))
    message2 = Text(Point(350, 350), msg2)
    message2.draw(win)

    # area

    s = (a + b + c)/2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    msg3 = "Area = " + str(round(area, 2))
    message3 = Text(Point(350, 400), msg3)
    message3.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to close")
    win.getMouse()

    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_text.draw(win)

    # entry box for red
    user_input1 = Entry(Point(win_width / 2 - 5, win_height / 2 + 40), 5)
    user_input1.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_text.draw(win)

    # entry box for green
    user_input2 = user_input1.clone()
    user_input2.move(0, 30)
    user_input2.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_text.draw(win)

    # entry box for blue
    user_input3 = user_input1.clone()
    user_input3.move(0, 60)
    user_input3.draw(win)

    output_text = Text(Point(7, 1), " ")
    output_text.draw(win)

    # display rgb text
    for i in range(5):
        win.getMouse()
        input_data1 = user_input1.getText()
        input_data2 = user_input2.getText()
        input_data3 = user_input3.getText()
        color = color_rgb(eval(input_data1), eval(input_data2), eval(input_data3))
        shape.setFill(color)

    # rgb

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = str(input("Enter a string: "))
    first = string[0]
    print(first)
    second = string[-1]
    print(second)
    third = string[1:5]
    print(third)
    fourth = string[0] + string[-1]
    print(fourth)
    fifth = string[0:3] * 10
    print(fifth)
    for i in range(len(string)):
        print(string[i])
    seventh = len(string)
    print(seventh)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, 7.2]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 3
    print(x)
    x = values[2:5]
    print(x)
    x = values[2] + values[0] + values[5]
    print(x)


def main():
    # target()
    # triangle()
    # color_shape()
    # process_string()
    # process_list()
    pass


main()
