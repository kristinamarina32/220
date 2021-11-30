"""
Name: Kristina Rydbom
lab13.py

Problem: Capstone for lab 13.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(file_name):
    # open file
    infile = open(file_name, "r")
    # read line
    read = infile.readline()
    # split by spaces
    split = read.split(" ")
    # stuff --
    count = 0
    for num in split:
        num = int(num)
        count = count + 1
        if num > 830:
            print("Warning! Trading volume exceeds 830 at", count, "seconds!")
        if num == 500:
            print("Pay attention! Volume equals 500 at", count, "seconds!")

    infile.close()


def main():
    trade_alert("trades.txt")
    pass


main()
