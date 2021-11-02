"""
Name: Kristina Rydbom
lab9.py

Problem: Complete lab 9 problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

def addTens(nums):
    for i in range(len(nums)):
        nums[i] = (nums[i]) + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = (nums[i]) ** 2


def sumList(nums):
    total = 0
    for i in range(len(nums)):
        add = (nums[i])
        total = total + add
    return total


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])


def writeSumOfSquares():
    in_file_name = input("Enter name of input file with at least two numbers on each line (be sure to include .txt): ")
    infile = open(in_file_name, "r")
    outfile = open("sum_out.txt", "w")
    for line in infile:
        each = line.split(" ")
        toNumbers(each)
        squareEach(each)
        total = sumList(each)
        print("Sum of squares = ", total, file=outfile)
    infile.close()
    outfile.close()


def starter():
    weight = float(input("Enter weight: "))
    numWins = int(input("Enter number of wins: "))
    if ((weight >= 150 and weight < 160) and numWins >= 5) or weight > 199 or numWins > 20:
        print("You should start")
    else:
        print("You should not start")


def leapYear(year):
    if (year % 4 == 0 and not(year % 100 == 0)) or year % 400 == 0:
        return True
    else:
        return False


def circleOverlap():
    win = GraphWin("Overlap!", 600, 600)

    point_a = Point(300, 200)

    center = win.getMouse()
    c1x = center.getX()
    c1y = center.getY()
    edge = win.getMouse()
    e1x = edge.getX()
    e1y = edge.getY()
    distance = ((c1x - e1x) ** 2 + (c1y - e1y) ** 2) ** (1/2)
    radius = distance
    circle_a = Circle(center, radius)
    circle_a.setOutline("red")

    circle_b = Circle(point_a, 40)
    circle_b.setOutline("purple")
    circle_a.draw(win)
    circle_b.draw(win)
    if (radius + 40) > (center + point_a)
        print("They overlap")
    else:
        print("They do not overlap")

    win.getMouse()
    win.getMouse()
    win.close()



def main():
    # function one
    # nums = [1,3,5]
    # print(nums)
    # addTens(nums)
    # print(nums)
    # function two
    # nums = [1, 3, 5]
    # print(nums)
    # squareEach(nums)
    # print(nums)
    # function three
    # nums = [1,3,5]
    # print(nums)
    # print(sumList(nums))
    # function four
    # strList = ["2","4","6"]
    # print(strList)
    # toNumbers(strList)
    # print(strList)
    # function five
    # writeSumOfSquares()
    # function six
    # starter()
    # function seven
    # leapYear(2000)
    # circleOverlap()

    pass


main()
