"""
Name: Kristina Rydbom
vigenere.py

Problem: Create a Vigenere Cipher.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def input(message):
    message = message.upper()
    message = message.replace(" ", "")
    return message


def code(message, keyword):
    sentence = str(input(message))
    kw = str(input(keyword))
    key_list = []
    for i in range(len(sentence)):
        sen = sentence[i]
        key = i % len(kw)
        change = ord(sen) - 65
        encryption = ord(kw[key]) - 65
        encoder = chr(((change + encryption) % 26) + 65)
        key_list.append(encoder)
    text = "".join(key_list)
    return text


def main():
    win = GraphWin("Vigenere Cipher", 600, 600)

    # Message text
    p1 = Point(160, 150)
    msg1 = Text(p1, "Message to code:")
    msg1.draw(win)

    # Keyword text
    p2 = Point(160, 200)
    msg2 = Text(p2, "Enter the keyword:")
    msg2.draw(win)

    # Entries
    message = Entry(Point(300, 150), 20)
    message.setText(" ")
    message.draw(win)
    msg = str(message)

    keyword = Entry(Point(300, 200), 20)
    keyword.setText(" ")
    keyword.draw(win)
    key = str(keyword)

    # Button
    button = Text(Point(300, 350), "Encode")
    button.draw(win)
    rec = Rectangle(Point(250, 330), Point(350, 370))
    rec.draw(win)

    win.getMouse()

    button.undraw()
    rec.undraw()

    # Resulting message
    msg3 = Text(Point(300, 300), "Resulting Message:")
    msg3.draw(win)

    encoded = Text(Point(300, 350), code(msg, key))
    encoded.draw(win)

    # Close window
    close = Point(300, 450)
    msg4 = Text(close, "Click anywhere to close")
    msg4.draw(win)

    win.getMouse()

    win.close()


if __name__ == '__main__':
    main()