"""
Name: Kristina Rydbom
algorithms.py

Problem: Algorithms for lab 12.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


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
        return my_list
    # close file
    my_file.close()


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        i = i + 1
        if i == search_val:
            return True
    return False


def main():
    read_data("read_data_test_data.txt")
    values = [1, 2, 3, 4, 5, 22, 7]
    is_in_linear(5, values)
    # add other function calls here
    pass


main()
