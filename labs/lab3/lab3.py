import math
"""
Name: Kristina Rydbom
lab3.py

Problem: Solving lab 3 problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    num_of_grades = eval(input("Enter number of grades to input:"))
    avg = 0
    for i in range(1, num_of_grades + 1):
        grade = eval(input("Enter grade " + str(i) + ":"))
        avg = avg + (grade / num_of_grades)
    print("Grade Average =", avg)


def tip_jar():
    total_sum = 0
    for i in range(1, 6):
        donation = eval(input("Enter donation " + str(i) + ":"))
        total_sum = total_sum + donation
    print("Total amount in the tip jar:", "$", total_sum)


def newton():
    x = eval(input("Enter value for x:"))
    num_approx = eval(input("Input how many times to improve the approximation:"))
    approx = x / 2
    for i in range(1, num_approx + 1):
        approx = ((approx + (x / approx)) / 2)
    print("Final value of the approximation:", approx)


def sequence():
    num_of_terms = eval(input("Enter the number of terms in a series:"))
    total_num = 1
    for i in range(num_of_terms):
        total_num = (i % 2) * 2 + total_num
        print(total_num, end="\t")


def pi():
    n = eval(input("Enter the number of terms in the series:"))
    number_pi = 1
    for i in range(n):
        numerator = ((((i + 1) % 2) * 2) + number_pi)
        print(numerator, end="\t")

