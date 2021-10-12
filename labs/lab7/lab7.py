""""
Name: Kristina Rydbom
lab7.py

Problem: Complete lab 7 problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def cash_conversion():
    num = eval(input("Enter an integer: "))
    one = num
    print("Corresponding dollar value: ", "$", "{:.2f}".format(one))


def encode():
    message = str(input("Enter the message to be encoded: "))
    key = eval(input("Enter an integer key value: "))
    for i in range(len(message)):
        ordinal = ord(message[i])
        combo = ordinal + key
        character = chr(combo)
        print(character, end="")


def sphere_area(radius):
    equation = 4 * math.pi * radius**2
    surface_area = round(equation, 2)
    return surface_area


def sphere_volume(radius):
    equation = (4/3) * math.pi * radius**3
    volume = round(equation, 2)
    return volume


def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_n_cubes(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i * i
    return total


def encode_better():
    message = str(input("Enter the message: "))
    key = str(input("Enter a key: "))
    for i in range(len(message)):
        ordinal = ord(message[i])
        shift = ord(key[i % len(key)]) - 97
        combo = ordinal + shift
        character = chr(combo)
        print(character, end="")


def main():
    # cash_conversion()
    # encode()
    # sphere_area(2)
    # sphere_volume(2)
    # sum_n(5)
    # sum_n_cubes(5)
    # encode_better()
    pass


main()
