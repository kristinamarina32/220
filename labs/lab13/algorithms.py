"""
Name: Kristina Rydbom
algorithms.py

Problem: Algorithms for lab 13.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
# from graphics import *


def read_data(filename):
    my_file = open(filename, "r")
    i = 0
    lines = my_file.readlines()
    my_list = []
    while i < len(lines):
        separate = lines[i].split()
        i = i + 1
        j = 0
        while j < len(separate):
            # convert to numbers
            val = eval(separate[j])
            # append
            my_list.append(val)
            j = j + 1
    # close file
    my_file.close()
    return my_list


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        i = i + 1
        if i == search_val:
            return True
    return False


def is_in_binary(search_val, values):
    left = 0
    right = len(values) - 1
    while left <= right:
        middle = (left + right)//2
        middle_value = values[middle]
        # more efficient way to do this: vvv
        # if search_val == middle_value:
        #     return True
        # elif search_val < middle_value:
        #     right = middle - 1
        # else:
        #     left = middle + 1
        if search_val == middle_value:
            return True
        if search_val < middle_value:
            right = middle - 1
        if search_val > middle_value:
            left = middle + 1
    return False


def selection_sort(values):
    # sort numbers into order
    length = len(values)
    # For each position in the list
    for i in range(length - 1):
        # find the smallest  in the list
        smallest = i
        for num in range(i + 1, length):  # as each one (val) goes (through the length), check if statement
            if values[num] < values[smallest]:  # if the num as it goes through < val, val now = num (which is smaller)
                smallest = num
        # swap smallest item to the bottom
        values[i], values[smallest] = values[smallest], values[i]


def calc_area(rect):
    # calculates the area of a graphics rectangle object
    point_1 = rect.getP1()
    point_2 = rect.getP2()
    x1 = point_1.getX()
    y1 = point_1.getY()
    x2 = point_2.getX()
    y2 = point_2.getY()
    length = (x2 - x1)**2
    width = (y2 - y1)**2
    area = length * width
    return area


def rect_sort(rectangles):
    length = len(rectangles)
    for i in range(length - 1):
        smallest = i
        # finds the area of each individual rectangle object with help from calc_area vvv
        # for example: --> i_area = calc_area(rectangles[i])
        for num in range(i + 1, length):
            if calc_area(rectangles[num]) < calc_area(rectangles[smallest]):
                smallest = num
        rectangles[i], rectangles[smallest] = rectangles[smallest], rectangles[i]


def main():
    # read_data("read_data_test_data.txt")
    # values = [1, 9, 3, 13, 5, 22, 7]
    # # is_in_linear(5, values)
    # # is_in_binary(4, values)
    # selection_sort(values)
    # # calc_area(rect)
    # rec1 = Rectangle(Point(200, 300), Point(400, 500))
    # rec2 = Rectangle(Point(100, 150), Point(400, 300))
    # rec3 = Rectangle(Point(60, 50), Point(200, 100))
    # rectangles = [rec1, rec2, rec3]
    # rect_sort(rectangles)
    pass


main()
