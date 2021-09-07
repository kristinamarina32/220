import math
"""
Name: Kristina Rydbom
lab2.py

Problem: Lab 2 Arithmetic problems.
"""


def sum_of_threes():
    upper_bound = eval(input("Enter an upper bound:"))
    total_sum = 0
    for i in range(0, (upper_bound + 1), 3):
        total_sum = total_sum + i
    print("The total sum of numbers 1-15 is:", total_sum)


def multiplication_table():
    print("Multiplication table for numbers 1 through 10:")
    print("   1 2 3 4 5 6 7 8 9 10")
    for row in range(1, 11):
        print(str(row)+":", end=" ")
        for column in range(1, 11):
            print(row * column, end=" ")
        print()


def triangle_area():
    a = eval(input("Enter side a:"))
    b = eval(input("Enter side b:"))
    c = eval(input("Enter side c:"))
    s = (a + b + c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the triangle:", area)


def sumSquares():
    lower_range = eval(input("Input lower range:"))
    upper_range = eval(input("Input upper range:"))
    sum_of_squares = 0
    for var in range(lower_range, upper_range + 1):
        sum_of_squares = sum_of_squares + var**2
    print("The sum of the squares is:", sum_of_squares)


def power():
    base = eval(input("Input base:"))
    exponent = eval(input("Input exponent:"))
    calculated_power = 1
    for var in range(exponent):
        calculated_power = calculated_power * base
    print(calculated_power)













